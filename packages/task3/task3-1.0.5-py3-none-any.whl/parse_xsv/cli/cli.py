import argparse
import csv
import json
import re
import sys
from abc import abstractmethod
from enum import Enum
from pathlib import Path
from typing import Optional, List

from parse_xsv.parse_xsv import set_log_level, logger, packet_version, QuotingTypes, ReaderXSV


class RegexPatterns(Enum):
    IP4 = \
        re.compile(r'\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}'
                   r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b')

    IP4_PRIVATE = \
        re.compile(r'\b(?=10|010|192.168|172.16|172.016)'
                   r'(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}'
                   r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b')

    IP4_CIDR = \
        re.compile(r'\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}'
                   r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b'
                   r'/\b(?:\d|[12]\d|3[0-2])\b')

    IP6 = \
        re.compile(r'(?<![.:\w])'
                   r'(?:(?P<canonical>(?:[A-F\d]{1,4}:){7}[A-F\d]{1,4})|'
                   r'(?P<omit_middle>(?:[\dA-F]{1,4}:){1,6}(?::[\dA-F]{1,4}){1,6})|'
                   r'(?P<omit_end>(?:[A-F\d]{1,4}:){1,7}:)|'
                   r'(?P<omit_start>:(?::[A-F\d]{1,4}){1,7}))'
                   r'(?![.:\w])',
                   flags=re.RegexFlag.I)

    IP6_PRIVATE = \
        re.compile(r'(?<![.:\w])'
                   r'(?=F[CD])'
                   r'(?:(?P<canonical>(?:[A-F\d]{1,4}:){7}[A-F\d]{1,4})|'
                   r'(?P<omit_middle>(?:[\dA-F]{1,4}:){1,6}(?::[\dA-F]{1,4}){1,6})|'
                   r'(?P<omit_end>(?:[A-F\d]{1,4}:){1,7}:)|'
                   r'(?P<omit_start>:(?::[A-F\d]{1,4}){1,7}))'
                   r'(?![.:\w])',
                   flags=re.RegexFlag.I)

    IP6_CIDR = \
        re.compile(r'(?<![.:\w])'
                   r'(?:(?P<canonical>(?:[A-F\d]{1,4}:){7}[A-F\d]{1,4})|'
                   r'(?P<omit_middle>(?:[\dA-F]{1,4}:){1,6}(?::[\dA-F]{1,4}){1,6})|'
                   r'(?P<omit_end>(?:[A-F\d]{1,4}:){1,7}:)|'
                   r'(?P<omit_start>:(?::[A-F\d]{1,4}){1,7}))'
                   r'(?![.:\w])'
                   r'/(?P<mask>12[0-8]|1[0-1]\d|\d\d|\d)\b',
                   flags=re.RegexFlag.I)

    MASK = \
        re.compile(r'\b(?:(?:0{1,3}|128|192|224|24[08]|25[245])\.){3}'
                   r'(?:0{1,3}|128|192|224|24[08]|25[245])\b')

    MAC = \
        re.compile(r'\b[A-Z\d]{2}(?P<delimiter>[:\-.])'
                   r'(?:[A-Z\d]{2}(?P=delimiter)){4}'
                   r'[A-Z\d]{2}\b',
                   flags=re.RegexFlag.I)

    MAC_LINUX = \
        re.compile(r'\b(?:[A-Z\d]{2}-){5}[A-Z\d]{2}\b',
                   flags=re.RegexFlag.I)

    MAC_WINDOWS = \
        re.compile(r'\b(?:[A-Z\d]{2}:){5}[A-Z\d]{2}\b',
                   flags=re.RegexFlag.I)

    MAC_CISCO = \
        re.compile(r'\b(?:[A-Z\d]{2}\.){5}[A-Z\d]{2}\b',
                   flags=re.RegexFlag.I)

    DOMAIN = \
        re.compile(r'(?<![.:\w])(?P<tld>\*?\.[a-z\d-]+)+(?![/.:\w])',
                   flags=re.RegexFlag.I)

    TLD = \
        re.compile(r'(?<![.:\w])(?P<tld>\*?\.[a-z\d-]+)(?![/.:\w])',
                   flags=re.RegexFlag.I)

    DOMAIN_SECOND = \
        re.compile(r'(?<![.:\w])(?P<tld>\*?\.[a-z\d-]+){2}(?![/.:\w])',
                   flags=re.RegexFlag.I)

    EMAIL = \
        re.compile(r'\b[\w!#$%&''*+/=?`{|}~^-]+'
                   r'(?:\.[\w!#$%&''*+/=?`{|}~^-]+)*'
                   r'@(?:[A-Z\d-]+\.)+[A-Z]{2,6}\b',
                   flags=re.RegexFlag.I)

    URI = \
        re.compile(r'(?P<scheme>[a-z][a-z\d+\-.]*:)+'
                   r'/{0,3}'
                   r'(?P<user>[a-z\d\-._~%!$&\'()*+,:;=]+@)?'
                   r'(?P<address>('
                   r'(?P<ipv6_host>\[[a-f\d:.]+])'
                   r'|[a-z\d-]+(?P<tld>\.[a-z\d-]+)+(?P<port>:\d+)?)'
                   r'|(?P<digit_address>[\d\-+]+))'
                   r'(?P<path>/[a-z\d\-._~%!$&\'()*+,;=:@]+)*/?'
                   r'(?P<question_query>\?[a-z\d\-._~%!$&\'()*+,;=:@/?]*)?'
                   r'(?P<hash_query>#[a-z\d\-._~%!$&\'()*+,;=:@/?]*)?',
                   flags=re.RegexFlag.I)

    URL = \
        re.compile(r'(?P<title>(?:https?|ftp)://|file:///?'
                   r'|(?P<user_w_wwwftp>[a-z\d\-._~%!$&\'()*+,:;=]+@)?(?:www|ftp)\.)'
                   r'(?P<user>[a-z\d\-._~%!$&\'()*+,:;=]+@)?'
                   r'[a-z\d-]+'
                   r'(?P<tld>\.[a-z0-9-]+)+'
                   r'(?P<port>:\d+)?'
                   r'(?P<path>/[a-z\d\-._~%!$&\'()*+,;=:@]+)*/?'
                   r'(?P<question_query>\?[a-z\d\-._~%!$&\'()*+,;=:@/?]*)?'
                   r'(?P<hash_query>#[a-z\d\-._~%!$&\'()*+,;=:@/?]*)?',
                   flags=re.RegexFlag.I)

    SSH_KEY = \
        re.compile(r'\b\s*(\bBEGIN\b).*(KEY\b)\s*\b',
                   re.RegexFlag.I)

    SSH_PRIVATE = \
        re.compile(r'\b\s*(\bBEGIN\b).*(PRIVATE KEY\b)\s*\b',
                   re.RegexFlag.I)

    SSH_PUBLIC = \
        re.compile(r'\b\s*(\bBEGIN\b).*(PUBLIC KEY\b)\s*\b',
                   re.RegexFlag.I)

    CARD = \
        re.compile(r'\b(?:(?P<visa>4\d{3}(?P<visa_space>[^\S\n\r]|-?)(\d{4}(?P=visa_space)){2}\d(?:\d{3})?)|'
                   r'(?P<mastercard>5[1-5]\d{2}'
                   r'(?P<mastercard_space>[^\S\n\r]|-?)(?:\d{4}(?P=mastercard_space)){2}\d{4})|'
                   r'(?P<discover>6(?:011|5\d{2})'
                   r'(?P<discover_space>[^\S\n\r]|-?)(?:\d{4}(?P=discover_space)){2}\d{4})|'
                   r'(?P<amex>3[47]\d{2}(?P<amex_space>[^\S\n\r]|-?)\d{6}(?P=amex_space)\d{5})|'
                   r'(?P<diners>3(?:0[0-5]|[68]\d)\d'
                   r'(?P<diners_space>[^\S\n\r]|-?)\d{6}(?P=diners_space)\d{4})|'
                   r'(?P<jcb>(?:2131|1800|35\d{3})\d{11}))\b')

    UUID = \
        re.compile(r'\b[A-F\d]{8}-(?:[A-F\d]{4}-){3}-[A-F\d]{12}\b',
                   flags=re.RegexFlag.I)


class Argument:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs


class Group:
    def __init__(self, title, description: str = None,
                 required: bool = False,
                 arguments: List[Argument] = None):
        self.title = title
        self.description = description
        self.required = required
        self.arguments = arguments


class Command:
    def __init__(self, prog_name: str = None,
                 help_epilog: str = None,
                 help_formatter=argparse.RawDescriptionHelpFormatter,
                 base_arg: List[Argument] = None,
                 groups: List[Group] = None,
                 mutually_groups: List[Group] = None,
                 argv: Optional[str] = None) -> None:
        self.argv = argv or sys.argv[:]
        self.prog_name = prog_name if prog_name else Path(self.argv[0]).name

        base_arg = base_arg if base_arg else []
        groups = groups if groups else []
        mutually_groups = mutually_groups if mutually_groups else []

        self.arguments = self.__parse_args(epilog=help_epilog,
                                           formatter=help_formatter,
                                           base_arg=base_arg,
                                           groups=groups,
                                           mutually_groups=mutually_groups)

    def __parse_args(self, epilog, formatter,
                     base_arg: List[Argument],
                     groups: List[Group],
                     mutually_groups: List[Group]) -> argparse.Namespace:
        parser = argparse.ArgumentParser(
            prog=self.prog_name,
            description=f"{self.prog_name} version {packet_version()}",
            epilog=epilog,
            formatter_class=formatter
        )

        [parser.add_argument(*val.args, **val.kwargs) for val in base_arg]

        for grp in groups:
            group = parser.add_argument_group(grp.title, grp.description)
            [group.add_argument(*val.args, **val.kwargs) for val in grp.arguments]

        for mut_grp in mutually_groups:
            group = parser.add_mutually_exclusive_group(required=mut_grp.required)
            [group.add_argument(*val.args, **val.kwargs) for val in mut_grp.arguments]

        return parser.parse_args(self.argv[1:])

    @abstractmethod
    def execute(self) -> None:
        """
        Perform code based on argument values.
        """
        pass


class CommandCLI(Command):
    def __quoting_value__(self, value: str) -> str:
        q_type = QuotingTypes[self.arguments.quoting]

        if value and '\n' in value and q_type != QuotingTypes.QUOTE_NONE or q_type == QuotingTypes.QUOTE_ALL:
            return f'"{value}"'
        else:
            return value

    def execute(self) -> None:
        set_log_level(self.arguments.v)

        logger.info(f'The CLI for parsing xSV files has been launched.')

        logger.debug('Argument values:')
        [logger.debug(f'{arg_name}: {getattr(self.arguments, arg_name)}') for arg_name in vars(self.arguments)]

        if self.arguments.file_name.name.find('stdin') != -1 and sys.stdin.isatty():
            logger.warning('File has not been passed and stdin is empty. Let\'s finish.')
            exit()  # File hasn't been passed and stdin is empty

        c_regex = None
        if self.arguments.col_regex:
            c_regex = [(el.split(',')[0], RegexPatterns[el.split(',')[1]].value,)
                       for el in self.arguments.col_regex]  # Replace reg name with reg expression in col_regex attrib
            logger.debug(f"""Convert col_regex argument {self.arguments.col_regex} to list
                         of tuples with regex expressions: {c_regex}""")

        s_regex = RegexPatterns[self.arguments.search_regex].value if self.arguments.search_regex else None
        logger.debug(f"""Convert search_regex argument {self.arguments.search_regex}
                                    to regex expression: {s_regex}""")

        output = list(ReaderXSV(self.arguments.file_name,
                                pure=self.arguments.pure,
                                no_header=self.arguments.no_header,
                                search_string=self.arguments.search,
                                search_regex=s_regex,
                                column_regex=c_regex,
                                rows=self.arguments.rows,
                                columns=self.arguments.columns,
                                restkey='rest',
                                delimiter=self.arguments.delimiter,
                                dialect=self.arguments.dialect,
                                quoting=QuotingTypes[self.arguments.quoting].value,
                                json=self.arguments.json,
                                strict=not self.arguments.force))

        logger.info(f'Output was generated')
        logger.debug(f"""with the following arguments:
                                    pure={self.arguments.pure},
                                    no_header={self.arguments.no_header},
                                    search_string={self.arguments.search},
                                    search_regex={s_regex},
                                    column_regex={c_regex},
                                    rows={self.arguments.rows},
                                    columns={self.arguments.columns},
                                    restkey={'rest'},
                                    delimiter={self.arguments.delimiter},
                                    dialect={self.arguments.dialect},
                                    quoting={QuotingTypes[self.arguments.quoting].value},
                                    json={self.arguments.json},
                                    strict={not self.arguments.force}""")

        if self.arguments.json:
            output = {'rows': output}
            output_file = json.dumps(output, indent=4)
        else:
            # logger.debug(output)
            output_file = [self.arguments.delimiter.join([self.__quoting_value__(str(el)) for el in ln])
                           for ln in output]
            output_file = '\n'.join(output_file)

        print(output_file)

        self.arguments.file_name.close()


ARGUMENTS = [
    Argument("--version", action="version", version=f"%(prog)s {packet_version()}"),

    Argument('-d', '--delimiter',
             dest='delimiter',
             metavar='',
             type=str,
             default=',',
             help='Specifies values separator (default: ",")'),

    Argument('-D', '--dialect',
             dest='dialect',
             metavar='',
             choices=csv.list_dialects(),
             help=f"""The xsv dialect type. Possible values:
             {','.join(csv.list_dialects())}"""),

    Argument('-j', '--json',
             dest='json',
             action='store_true',
             help='Show output in JSON format. If filename is passed'),

    Argument('-p', '--pure',
             dest='pure',
             action='store_true',
             help='Using pure Python library parsing without CSV module'),

    Argument('-q', '--quoting',
             dest='quoting',
             metavar='',
             choices=[e.name for e in QuotingTypes],
             default='QUOTE_MINIMAL',
             help=f"""How values are quoted in the CSV file (default: QUOTE_MINIMAL).
             Possible values could be:
             {', '.join([e.name for e in QuotingTypes])}"""),

    Argument('--no-header',
             dest='no_header',
             action='store_true',
             help='Whether parsing CSV file(s) contains a header or not'),

    Argument('--force',
             dest='force',
             action='store_true',
             help='Forcibly process an ill-formed format input file'),

    Argument('-v',
             action='count',
             default=0,
             help='Increase verbosity level (add more v)'),

    Argument('-c', '--columns',
             dest='columns',
             nargs='*',
             metavar='INDEXES',
             type=str,
             help="""The column range from the xCV file to be output
             You can pass values in the following formats:
             particular indexes: index1 index2 ... indexN
             range of indexes: index1-index2
             from the beginning up to index: -index
             from index to the end: index-"""),

    Argument('-r', '--rows',
             dest='rows',
             nargs='*',
             metavar='INDEXES',
             type=str,
             help="""The row range from the xCV file to be output. 
             You can pass values in the following formats:
             particular indexes: index1 index2 ... indexN
             range of indexes: index1-index2
             from the beginning up to index: -index
             from index to the end: index-"""),

    Argument('file_name',
             nargs='?',
             type=argparse.FileType('r'),
             default='-',
             help='An input filename'),
]

ARGUMENTS_MUTUAL_GROUPS = [
    Group('search_group',
          arguments=[
              Argument('-C', '--col-regex',
                       dest='col_regex',
                       nargs='*',
                       metavar='REGEX',
                       help=f"""Find rows based on a given regex string in specific columns.
                       You can pass values in the following formats:
                       particular indexes: index1,regex1 index2,regex2 ... indexN,regexN
                       range of indexes: index1-index2,regex
                       from the beginning up to index: -index,regex
                       from index to the end: index-,regex                       
                       
                       Possible values could be:
                       {', '.join([e.name for e in RegexPatterns])}"""),

              Argument('-s', '--search',
                       dest='search',
                       metavar='SEARCH',
                       help='Find rows based on a given search string'),

              Argument('-S', '--search-regex',
                       dest='search_regex',
                       metavar='REGEX',
                       choices=[e.name for e in RegexPatterns],
                       help=f"""Find rows based on a given regex.
                       Possible values could be:
                       {', '.join([e.name for e in RegexPatterns])}"""),
          ]),
]


def parse_cli(argv: Optional[str] = None) -> None:
    # sys.stdout.reconfigure(encoding="utf-8")

    if sys.stdout.encoding is None:
        print(
            "please set python env PYTHONIOENCODING=UTF-8, example: "
            "export PYTHONIOENCODING=UTF-8, when writing to stdout",
            file=sys.stderr,
        )
        exit(1)

    command = CommandCLI('parse_xsv',
                         base_arg=ARGUMENTS,
                         mutually_groups=ARGUMENTS_MUTUAL_GROUPS,
                         argv=argv)
    command.execute()


if __name__ == '__main__':
    parse_cli()
