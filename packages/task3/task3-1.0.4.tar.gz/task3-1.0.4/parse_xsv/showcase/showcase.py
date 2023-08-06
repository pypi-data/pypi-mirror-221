import os
import platform
import subprocess
import sys
import time
from typing import Dict, List, Optional, Union

import questionary
import select
from questionary import prompt, Choice

from parse_xsv import set_log_level, logger
from parse_xsv.cli import RegexPatterns, Command, Argument
from parse_xsv.parse_xsv import packet_version

if sys.platform.startswith('win32'):
    import msvcrt


class CommandShowcase(Command):
    __intro__ = '''
    ███    ███  ██████  ██████  ██    ██ ██      ███████     ██████         
    ████  ████ ██    ██ ██   ██ ██    ██ ██      ██               ██ ██     
    ██ ████ ██ ██    ██ ██   ██ ██    ██ ██      █████        █████         
    ██  ██  ██ ██    ██ ██   ██ ██    ██ ██      ██          ██      ██     
    ██      ██  ██████  ██████   ██████  ███████ ███████     ███████        
                                                                            
                                                                            
        ██████  ██    ██ ████████ ██   ██  ██████  ███    ██                
        ██   ██  ██  ██     ██    ██   ██ ██    ██ ████   ██                
        ██████    ████      ██    ███████ ██    ██ ██ ██  ██                
        ██         ██       ██    ██   ██ ██    ██ ██  ██ ██                
        ██         ██       ██    ██   ██  ██████  ██   ████                
                                                                            
                                                                            
    ████████  █████  ███████ ██   ██     ██████   █████        ██████       
       ██    ██   ██ ██      ██  ██           ██ ██   ██       ██   ██      
       ██    ███████ ███████ █████        █████  ███████ █████ ██████       
       ██    ██   ██      ██ ██  ██           ██ ██   ██       ██   ██      
       ██    ██   ██ ███████ ██   ██     ██████  ██   ██       ██████       
    '''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.__command_key_name__ = 'module_command' if self.arguments.as_module else 'command'

    @staticmethod
    def __wait_for_input__(timeout):
        start_time = time.time()
        input_str = ""

        try:
            if sys.platform.startswith('win'):
                while True:
                    if msvcrt.kbhit():
                        char = msvcrt.getwch()
                        if char == '\r':  # Check for Enter key
                            input_str += 'Enter'
                        else:
                            input_str += char
                        break
                    elif time.time() - start_time >= timeout:
                        break
                    time.sleep(0.1)  # Adjust the sleep duration as needed

            else:  # Unix-based systems (Linux, macOS)
                while True:
                    # Check if there is input available to read
                    if sys.stdin in select.select([sys.stdin], [], [], timeout)[0]:
                        char = sys.stdin.read(1)
                        if char == '\n':  # Check for Enter key
                            input_str += 'Enter'
                        else:
                            input_str += char
                        break
                    elif time.time() - start_time >= timeout:
                        break
                    time.sleep(0.1)  # Adjust the sleep duration as needed
        except KeyboardInterrupt:
            exit()

        return input_str.strip()

    # noinspection DuplicatedCode
    def packet_output(self) -> None:
        command_packet = [
            *[
                (val.get('descr', ''),
                 val.get(self.__command_key_name__, '').format(
                     *[
                         arg.get('default', '') if 'filter' not in arg
                         else arg.get('filter', lambda x: '')(arg.get('default', ''))
                         for arg in val['arguments']
                     ]),
                 )
                if 'arguments' in val else val.get(self.__command_key_name__, '')
                for key, val in OPTIONS.items() if val.get(self.__command_key_name__, None)
            ],
            *[
                (o_val.get('descr', ''),
                 o_val.get(self.__command_key_name__, '').format(
                     *[
                         arg.get('default', '') if 'filter' not in arg
                         else arg.get('filter', lambda x: '')(arg.get('default', ''))
                         for arg in o_val['arguments']
                     ]),
                 )
                if 'arguments' in o_val else o_val.get(self.__command_key_name__, '')
                for key, val in OPTIONS.items() if 'options' in val
                for o_key, o_val in val['options'].items() if o_val.get(self.__command_key_name__, None)
            ]
        ]

        [self.__print_output__(el[1], el[0]) for el in command_packet]

    @staticmethod
    def __print_output__(command: str,
                         main_message='According to your choice, the command to be invoked will be:') -> None:

        if not command:
            return

        print(f'\n{main_message}')
        questionary.print(f'{command}', style='#009b06')

        result = subprocess.run(command, capture_output=True, text=True, shell=True)

        if result.stdout and result.stdout.strip():
            print('\nThe output is:')
            questionary.print(f'{result.stdout.strip()}', style='#009b06')

        if result.stderr:
            print('\nThe log messages are:')
            questionary.print(f'{result.stderr}', style='#009b06')

    def execute(self) -> None:
        set_log_level(self.arguments.v)

        logger.info(f'The parse_xsv library showcase.')

        logger.debug('Argument values:')
        [logger.debug(f'{arg_name}: {getattr(self.arguments, arg_name)}') for arg_name in vars(self.arguments)]

        if self.arguments.all:
            self.packet_output()
            exit()

        delay = 0.3
        for line in self.__intro__.splitlines():
            print(line)

            if delay and self.__wait_for_input__(delay):
                delay = 0

        time.sleep(3.3 * delay)

        answers = prompt(questions)
        command = ''.join(
            [
                *[
                    o_val.get(self.__command_key_name__, '').format(*[a_val for _, a_val in list(answers.items())[2:]])
                    for key, val in OPTIONS.items() if key == answers.get('category', None) and 'options' in val
                    for o_key, o_val in val['options'].items() if o_key == answers.get(key, None)
                ],
                *[
                    val.get(self.__command_key_name__, '').format(*[a_val for _, a_val in list(answers.items())[1:]])
                    for key, val in OPTIONS.items()
                    if key == answers.get('category', None) and 'arguments' in val and self.__command_key_name__ in val
                ],
            ]
        )

        self.__print_output__(command)


# Determine the platform
current_platform = platform.system()

# Set the Python command based on the platform
if current_platform == 'Windows':
    python_command = 'python -m'
else:
    python_command = 'python3 -m'

select_style = questionary.Style([
    #     ('default', "bg:#ffffff fg:#000000"),
    # ('selected', 'bg:#336699 fg:#ffffff'),
    ('highlighted', '#008888'),
    ('pointer', '#008888'),
    # ('question', 'fg:#009b06'),
    ('qmark', 'fg:#009b06'),
    ('instruction', "#008888"),
    ('answer', "#009b06"),
])

OPTIONS_ARGUMENTS = {
    'r': {
        'descr': 'r',
        'type': 'text',
        'message': 'Provide row range (row1 row2 ... rowN) (row1-rowN) (from the beginning: -row) (to the end: row-)',
        'default': '1-',
    },
    'c': {
        'descr': 'c',
        'type': 'text',
        'message': 'Provide column range (col1 col2 ... colN)(col1-colN)(from the beginning: -col)(to the end: col-)',
        'default': '1-',
    },
    's': {
        'descr': 's',
        'type': 'text',
        'message': 'Please, provide search string',
        'default': '255',
    },
    're': {
        'descr': 're',
        'type': 'select',
        'name': 'regex',
        'message': 'Which regular expression would you like to choose?',
        'choices': [Choice(title=val.name, value=val.name) for val in RegexPatterns],
        'instruction': '(Use arrow keys to navigate through the menu)',
        'pointer': '>',
        'filter': lambda val: val if val else 'IP4',
        'use_shortcuts': True,
    },
    'j': {
        'descr': 'j',
        'type': 'confirm',
        'message': 'Would you like to output in JSON format?',
        'default': False,
        'filter': lambda val: '-j' if val else '',
    },
    'j_true': {
        'descr': 'j_true',
        'type': 'confirm',
        'message': 'Would you like to output in JSON format?',
        'default': True,
        'filter': lambda val: '-j' if val else '',
    },
    'n': {
        'descr': 'n',
        'type': 'confirm',
        'message': 'Does not the parsed file contain a header on the first line?',
        'default': False,
        'filter': lambda val: '--no-header' if val else '',
    },
    'n_true': {
        'descr': 'n_true',
        'type': 'confirm',
        'message': 'Does not the parsed file contain a header on the first line?',
        'default': True,
        'filter': lambda val: '--no-header' if val else '',
    },
    'f': {
        'descr': 'f',
        'type': 'path',
        'message': 'Which file would you like to use?',
        'validation': lambda val: True if val else 'Please, provide a path to a file',
        'default': f'{os.path.dirname(os.path.abspath(__file__))}/sample.csv',
        'filter': lambda val: f'"{val}"' if val else val,
    },
    'f_tsv': {
        'descr': 'f_tsv',
        'type': 'path',
        'message': 'Which file would you like to use?',
        'validation': lambda val: True if val else 'Please, provide a path to a file',
        'default': f'{os.path.dirname(os.path.abspath(__file__))}/sample.tsv',
        'filter': lambda val: f'"{val}"' if val else val,
    },
    'f_out': {
        'descr': 'f_out',
        'type': 'path',
        'message': 'In which file would you like to write generated passwords (it may be new)?',
        'validation': lambda val: True if val else 'Please specify the path to the file',
        'default': './sample_output.csv',
        'filter': lambda val: f'"{val}"' if val else val,
    },
    'f_log': {
        'descr': 'f_log',
        'type': 'path',
        'message': 'In which file would you like to write log messages (it may be new)?',
        'validation': lambda val: True if val else 'Please specify the path to the file',
        'default': './parse_xsv.log',
        'filter': lambda val: f'"{val}"' if val else val,
    },
    'f_err': {
        'descr': 'f_err',
        'type': 'path',
        'message': 'Which file would you like to use?',
        'validation': lambda val: True if val else 'Please, provide a path to a file',
        'default': f'{os.path.dirname(os.path.abspath(__file__))}/corrupted_sample.csv',
        'filter': lambda val: f'"{val}"' if val else val,
    },
    'v': {
        'descr': 'v',
        'type': 'text',
        'message': 'What logging level would you like to set?',
        'default': '0',
        'validation': lambda val: True if val.isdigit() else 'Please, provide a number',
        'filter': lambda val: f'{"-" if int(val) > 0 else ""}{"v" * (int(val) if int(val) <= 3 else 3)}',
    },
}

# OPTIONS: Dict[str, Dict[str, str | List[Dict] | Dict[str, Dict[str, str | List[Dict]]]]] = {
OPTIONS: Dict[str, Dict[str, Union[str, List[Dict], Dict[str, Dict[str, Union[str, List[Dict]]]]]]] = {
    'charset': {
        'descr': 'different parsing options',
        'options': {
            'parse_default': {
                'descr': 'parse file with default parameters ',
                'command': 'parse_xsv {} {}',
                'module_command': f'{python_command} parse_xsv {{}} {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['v'], ],
            },
            'custom_rows': {
                'descr': 'output a range of rows to the screen',
                'command': 'parse_xsv {} -r{} {} {}',
                'module_command': f'{python_command} parse_xsv {{}} -r{{}} {{}} {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['r'],
                              OPTIONS_ARGUMENTS['j'], OPTIONS_ARGUMENTS['v'], ],
            },
            'custom_columns': {
                'descr': 'output custom columns',
                'command': 'parse_xsv {} -c{} {} {}',
                'module_command': f'{python_command} parse_xsv {{}} -c{{}} {{}} {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['c'],
                              OPTIONS_ARGUMENTS['j'], OPTIONS_ARGUMENTS['v'], ],
            },
            'no_header': {
                'descr': 'do not process the first line as a header',
                'command': 'parse_xsv {} {} {} {}',
                'module_command': f'{python_command} parse_xsv {{}} {{}} {{}} {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['n_true'],
                              OPTIONS_ARGUMENTS['j_true'], OPTIONS_ARGUMENTS['v'], ],
            },
            'delimiter': {
                'descr': 'parse a tsv (tabulator) file',
                'command': r'parse_xsv {} -d "	" {} {} {}',
                'module_command': rf'{python_command} parse_xsv {{}} -d "	" {{}} {{}} {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f_tsv'], OPTIONS_ARGUMENTS['n'],
                              OPTIONS_ARGUMENTS['j'], OPTIONS_ARGUMENTS['v'], ],
            },
            'ill_formed': {
                'descr': 'parse a file with an ill-formed format',
                'command': 'parse_xsv {} {} {} {}',
                'module_command': f'{python_command} parse_xsv {{}} {{}} {{}} {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f_err'], OPTIONS_ARGUMENTS['n'],
                              OPTIONS_ARGUMENTS['j'], OPTIONS_ARGUMENTS['v'], ],
            },
        },
    },
    'filtering': {
        'descr': 'parsing with filtering',
        'options': {
            'search_string': {
                'descr': 'filtering output based on a search string',
                'command': 'parse_xsv {} -s{} {} {}',
                'module_command': f'{python_command} parse_xsv {{}} -s{{}} {{}} {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['s'],
                              OPTIONS_ARGUMENTS['j'], OPTIONS_ARGUMENTS['v'], ],
            },
            'regex_search': {
                'descr': 'output rows with values equal a specific regex only',
                'command': 'parse_xsv {} -S{} {} {}',
                'module_command': f'{python_command} parse_xsv {{}} -S{{}} {{}} {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['re'],
                              OPTIONS_ARGUMENTS['j'], OPTIONS_ARGUMENTS['v'], ],
            },
            'column_regex': {
                'descr': 'output rows with values equal a specific regex in a specific columns',
                'command': 'parse_xsv {} -C {},{} {} {}',
                'module_command': f'{python_command} parse_xsv {{}} -C {{}},{{}} {{}} {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['c'],
                              OPTIONS_ARGUMENTS['re'], OPTIONS_ARGUMENTS['j'],
                              OPTIONS_ARGUMENTS['v'], ],
            },
        },
    },
    'pipe': {
        'descr': 'pipes with the parse_xsv command',
        'options': {
            'pipe_stdin': {
                'descr': 'pipe stdin from a file',
                'command': 'cat {} | parse_xsv -c{} {} {}',
                'module_command': f'cat {{}} | {python_command} parse_xsv -c{{}} {{}} {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['c'],
                              OPTIONS_ARGUMENTS['j'], OPTIONS_ARGUMENTS['v'], ],
            },
            'pipe_stdout': {
                'descr': 'pipe stdout to a file',
                'command': 'parse_xsv {} -c{} {} {} > {}',
                'module_command': f'{python_command} parse_xsv {{}} -c{{}} {{}} {{}} > {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['c'],
                              OPTIONS_ARGUMENTS['j'], OPTIONS_ARGUMENTS['v'],
                              OPTIONS_ARGUMENTS['f_out'], ],
            },
            'pipe_stderr': {
                'descr': 'pipe stderr to a file',
                'command': 'parse_xsv {} -c{} {} -vvv 2> {}',
                'module_command': f'{python_command} parse_xsv {{}} -c{{}} {{}} -vvv 2> {{}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['c'],
                              OPTIONS_ARGUMENTS['j'], OPTIONS_ARGUMENTS['f_log'], ],
            },
            'pipe_complex': {
                'descr': 'complex pipe with double call',
                'command': 'cat {0} | parse_xsv -s {1} {2} | parse_xsv {3} -c{4} {2}',
                'module_command': f'cat {{0}} | {python_command} parse_xsv -s {{1}} {{2}} '
                                  f'| {python_command} parse_xsv {{3}} -c {{4}} {{2}}',
                'arguments': [OPTIONS_ARGUMENTS['f'], OPTIONS_ARGUMENTS['s'],
                              OPTIONS_ARGUMENTS['v'], OPTIONS_ARGUMENTS['j_true'],
                              OPTIONS_ARGUMENTS['c'], ],
            },
        }
    },
}

questions = [
    {
        'type': 'select',
        'name': 'category',
        'message': 'Which xSV file parsing category would you like to choose?',
        'choices': [Choice(title=val['descr'], value=key) for key, val in OPTIONS.items()],
        'instruction': '(Use arrow keys to navigate through the menu)',
        'pointer': '>',
        'use_shortcuts': True,
        'style': select_style,
    },
    *[
        {
            'type': 'select',
            'name': key,
            'message': 'Which xSV file parsing approach would you like to choose?',
            'choices': [Choice(title=o_val['descr'], value=o_key) for o_key, o_val in val['options'].items()],
            'when': lambda x, key=key: x['category'] == key,
            'instruction': '(Use arrow keys to navigate through the menu)',
            'pointer': '>',
            'use_shortcuts': True,
            'style': select_style,
        } for key, val in OPTIONS.items() if 'options' in val
    ],
    *[
        {
            'type': a_val.get('type', 'text'),
            'name': f'{key}_{a_val.get("descr", "")}',
            'message': a_val.get('message', ''),
            'when': lambda x, key=key: x['category'] == key,
            'style': select_style,
            **({'choices': a_val['choices']} if 'choices' in a_val else {}),
            **({'filter': a_val['filter']} if 'filter' in a_val else {}),
            **({'validate': a_val['validation']} if 'validation' in a_val else {}),
            **({'default': a_val['default']} if 'default' in a_val else {}),
        }
        for key, val in OPTIONS.items() if 'options' not in val and 'arguments' in val
        for a_val in val['arguments']
    ],
    *[
        {
            'type': a_val.get('type', 'text'),
            'name': f'{o_key}_{a_val.get("descr", "")}',
            'message': a_val.get('message', ''),
            'when': lambda x, key=key, o_key=o_key: x.get(key, None) == o_key,
            'style': select_style,
            **({'choices': a_val['choices']} if 'choices' in a_val else {}),
            **({'filter': a_val['filter']} if 'filter' in a_val else {}),
            **({'validate': a_val['validation']} if 'validation' in a_val else {}),
            **({'default': a_val['default']} if 'default' in a_val else {}),
        }
        for key, val in OPTIONS.items() if 'options' in val
        for o_key, o_val in val['options'].items() if 'arguments' in o_val
        for a_val in o_val['arguments']
    ],
]

ARGUMENTS = [
    Argument("--version", action="version", version=f"%(prog)s {packet_version()}"),

    Argument('-m', '--module',
             dest='as_module',
             action='store_true',
             help='Invoke parse_xsv using python -m approach'),

    Argument('--all',
             dest='all',
             action='store_true',
             help='Show all use cases at once without any interaction'),

    Argument('-v',
             action='count',
             default=0,
             help='Increase verbosity level (add more v)'),
]


def parse_showcase(argv: Optional[str] = None):
    # sys.stdout.reconfigure(encoding="utf-8")

    if sys.stdout.encoding is None:
        print(
            "please set python env PYTHONIOENCODING=UTF-8, example: "
            "export PYTHONIOENCODING=UTF-8, when writing to stdout",
            file=sys.stderr,
        )
        exit(1)

    command = CommandShowcase('parse_xsv showcase',
                              base_arg=ARGUMENTS,
                              argv=argv)
    command.execute()


if __name__ == '__main__':
    parse_showcase()
