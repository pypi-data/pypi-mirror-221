import csv
import random
import sys
from typing import List, Optional, Tuple

from faker import Faker, documentor, exceptions

from parse_xsv import QuotingTypes
from parse_xsv.cli.cli import Argument, Command
from parse_xsv.parse_xsv import packet_version, set_log_level, logger


class CommandGenCLI(Command):
    __faker_methods__: List[str] = None

    @staticmethod
    def __get_faker_methods__() -> List[str]:
        """Generate a method list of Faker library methods"""
        fake = Faker()
        doc = documentor.Documentor(fake)

        unsupported: List[str] = []
        while True:
            try:
                formatters = doc.get_formatters(with_args=True, with_defaults=True, excludes=unsupported)
            except exceptions.UnsupportedFeature as e:
                unsupported.append(e.name)
            else:
                break

        return [''.join(el.replace('fake.', '').split('(')[:1])
                for _, fmt in formatters
                for el in fmt if el.find('fake.') != -1]

    @classmethod
    def faker_methods(cls) -> List[str]:
        """Getter/setter-initializer for the private static cache class argument __faker_methods__"""
        if cls.__faker_methods__ is None:
            cls.__faker_methods__ = cls.__get_faker_methods__()

        return cls.__faker_methods__

    def __parse_structure_arg__(self) -> List[Tuple]:
        """It parses a name,val string to the tuple of (name, val).
        If name was missed, the index is added instead of name (index, val)."""

        splitted = [str(val).split(',') for ind, val in enumerate(self.arguments.structure)]

        if any(er_el := [el for el in splitted if len(el) == 0 or len(el) > 2]):
            raise Exception(f'Wrong structure element(s) were passed: {er_el}')

        return \
            [
                (
                    str(index) if len(spl_lst) == 1 else spl_lst[0],
                    spl_lst[0] if len(spl_lst) == 1 else spl_lst[1],
                )
                for index, spl_lst in enumerate(splitted)
            ]

    def __broke_lines__(self, list_to_be_broken: List[List]) -> List[List]:
        """1. Randomly selects lines to be damaged.
        2. Randomly selects whether add or skip line elements (if line is short only add).
        3. If it needs to be added, Faker's random methods are utilized to add a random amount of data.
        4. If it needs to be skipped, a random number of line elements is skipped."""

        fake = Faker()
        ret = []

        for idx, line in enumerate(list_to_be_broken):
            if idx == 0 and not self.arguments.no_header:
                ret += [line]
                continue

            if not bool(random.getrandbits(1)):
                ret += [line]
                continue

            if bool(random.getrandbits(1)) and len(self.arguments.structure) > 3:
                skipped_el_num = random.choice(range(1, len(self.arguments.structure) - 2))
                ret += [[el for ind, el in enumerate(line)
                         if ind < len(self.arguments.structure) - skipped_el_num]]
            else:
                l_cp = line.copy()
                wrong_el_num = random.choice(range(1, 5))
                l_cp += [str(getattr(fake, random.choice(self.faker_methods()))())
                         for _ in range(0, wrong_el_num)]
                ret += [l_cp]

        return ret

    def __quoting_value__(self, value: str) -> str:
        q_type = QuotingTypes[self.arguments.quoting]

        if '\n' in value and q_type != QuotingTypes.QUOTE_NONE or q_type == QuotingTypes.QUOTE_ALL:
            return f'"{value}"'
        else:
            return value

    def execute(self) -> None:
        set_log_level(self.arguments.v)

        logger.info(f'The CLI for generating xSV files of the specified structure.')

        logger.debug('Argument values:')
        [logger.debug(f'{arg_name}: {getattr(self.arguments, arg_name)}') for arg_name in vars(self.arguments)]

        fake = Faker()

        structure = self.__parse_structure_arg__()
        logger.debug(f'Splitted structure of income structure argument: {structure}')

        output = []
        if not self.arguments.no_header:
            output += [[el[0] for el in structure]]
            logger.debug(f'The header of the xSV file: {output[0]}')

        for _ in range(0, self.arguments.rows):
            output += [[self.__quoting_value__(getattr(fake, el[1])()) for el in structure]]
            logger.debug(f'{self.arguments.rows} rows have been created.')

        if self.arguments.ill_formed:
            output = self.__broke_lines__(output)
            logger.debug('Previously generated rows have been corrupted.')

        logger.info(f'A new file has been generated with {len(structure)} columns and {self.arguments.rows} rows.')

        output_file = [self.arguments.delimiter.join(ln) for ln in output]
        output_file = '\n'.join(output_file)

        print(output_file)


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
             help='Whether generated CSV file contains a header or not'),

    Argument('-i', '--ill-formed',
             dest='ill_formed',
             action='store_true',
             help='Forcibly generate an ill-formed format file'),

    Argument('-v',
             action='count',
             default=0,
             help='Increase verbosity level (add more v)'),

    Argument('-r', '--rows',
             dest='rows',
             metavar='',
             type=int,
             default=1,
             help="""Number of rows to be generated"""),

    Argument('structure',
             nargs='+',
             help=f"""The list of column names and column types to be used as output file structure. 
             You can pass values in the following formats:
             just a type (column name will be index number): type1 type2 ... typeN
             column name + type: column_name1,typeN column_name2,typeN ... column_nameN,typeN
             
             Possible type values could be:
             {', '.join(CommandGenCLI.faker_methods())}"""),
]


def generate_sample_data(argv: Optional[str] = None):
    # sys.stdout.reconfigure(encoding="utf-8")

    if sys.stdout.encoding is None:
        print(
            "please set python env PYTHONIOENCODING=UTF-8, example: "
            "export PYTHONIOENCODING=UTF-8, when writing to stdout",
            file=sys.stderr,
        )
        exit(1)

    help_epilog = '''This generator generates an xSV file an print it to stdout. 
Mainly it will be displayed on your monitor screen.
If you want ot save generated data to file, please use > operator or pipe |.'''

    command = CommandGenCLI('sample_gen',
                            help_epilog=help_epilog,
                            base_arg=ARGUMENTS,
                            argv=argv)
    command.execute()


if __name__ == '__main__':
    generate_sample_data()
