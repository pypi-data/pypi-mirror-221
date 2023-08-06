import csv
import logging
from collections import Counter
from enum import Enum
from typing import Pattern, List, Tuple, Set

from typing.io import TextIO

from parse_xsv.__version__ import __version__

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)


class QuotingTypes(Enum):
    QUOTE_NONE = csv.QUOTE_NONE
    QUOTE_NONNUMERIC = csv.QUOTE_NONNUMERIC
    QUOTE_MINIMAL = csv.QUOTE_MINIMAL
    QUOTE_ALL = csv.QUOTE_ALL


class ReaderXSV(csv.DictReader):
    def __init__(self,
                 io: TextIO,
                 pure: bool = False,
                 no_header: bool = False,
                 search_string: str = None,
                 search_regex: Pattern[str] = None,
                 column_regex: List[Tuple] = None,
                 rows: List[str] = None,
                 columns: List[str] = None,
                 json: bool = False,
                 *args, **kwargs):
        super().__init__(io, *args, **kwargs)

        self.search_string = search_string
        self.search_regex = search_regex
        self.column_regex = column_regex if column_regex else []
        self.rows = rows if rows else []
        self.columns = columns if columns else []
        self.json = json

        self.__iterator__ = 0

        # if pure:
        #     self.reader = xsv_reader(io, *args, **kwargs)

        self.no_header = no_header
        if no_header and not self._fieldnames:
            self.__when_no_header__(io)

    def __when_no_header__(self, io: TextIO):
        try:
            len_lst = [len(line) for line in list(self.reader)]

            counter = Counter(len_lst)
            max_count = counter.most_common(1)[0][1]  # get the maximum count

            values = counter.most_common(None)  # get all the elements and their counts
            values = [x[0] for x in values if x[1] == max_count]  # filter by maximum count

            max_column = max(values)

            self._fieldnames = [str(i+1) for i in range(max_column)]

            io.seek(0, 0)
        except StopIteration:
            pass

    # noinspection PyMethodMayBeStatic
    def __check_column_regex__(self, line) -> bool:
        for el in self.column_regex:
            ind_lst = self.__transform_indexes__([el[0]], len(self._fieldnames))
            key_lst = [val for ind, val in enumerate(self._fieldnames) if ind + 1 in ind_lst]
            if self.json and not any({key: val for key, val in line.items()
                                      if key in key_lst and el[1].search(val)}):
                return False
            elif not self.json and not any([val for key, val in enumerate(line)
                                            if key + 1 in ind_lst and el[1].search(str(val))]):
                return False

        return True

    # noinspection PyMethodMayBeStatic
    def __transform_indexes__(self, lst: List[str], max_index: int) -> Set[int]:
        ret = set()
        for index in lst:
            if index.find('-', 1, len(index) - 1) != -1:
                rng = [int(part) for part in index.split('-')]
                if len(rng) != 2:
                    raise Exception(f'Wrong index range was passed {index}')

                ret = ret.union({el for el in range(rng[0], rng[1] + 1)})
            elif index[:1] == '-':
                ret = ret.union({el for el in range(1, int(index[1:]) + 1)})
            elif len(index) > 1 and index[-1] == '-':
                ret = ret.union({el for el in range(int(index.replace('-', '')), max_index + 1)})
            else:
                ret.add(int(index))

        return ret

    def __next__(self):
        if not self.json and not self.no_header and not self.__iterator__:
            names = self.fieldnames if self.fieldnames else []
            if names and self.columns:
                ind_lst = self.__transform_indexes__(self.columns, len(self._fieldnames))
                names = [val for key, val in enumerate(self.fieldnames) if key + 1 in ind_lst]

            self.__iterator__ += 1
            return names

        if self.json:
            ret = super().__next__()
        else:
            ret = self.__next_list__()

        self.__iterator__ += 1

        if not ret:
            return ret

        if self.json:
            ret = self.__filter_dict_row__(ret)
        else:
            ret = self.__filter_list_row__(ret)

        if not ret:
            return self.__next__()

        return ret

    def __filter_dict_row__(self, row) -> dict:
        if self.rows and self.__iterator__ not in self.__transform_indexes__(self.rows, self.__iterator__):
            row = {}

        if row and self.search_regex \
                and not any({key: val for key, val in row.items()
                             if self.search_regex.search(val)}):
            row = {}

        if row and self.search_string \
                and not any({key: val for key, val in row.items()
                             if str(val).find(self.search_string) != -1}):
            row = {}

        if row and self.column_regex and not self.__check_column_regex__(row):
            row = {}

        if row and self.columns:
            ind_lst = self.__transform_indexes__(self.columns, len(self._fieldnames))
            key_lst = [val for ind, val in enumerate(self._fieldnames) if ind + 1 in ind_lst]
            row = {key: val for key, val in row.items() if key in key_lst}

        return row

    def __filter_list_row__(self, row) -> List:
        if self.rows and self.__iterator__ not in self.__transform_indexes__(self.rows, self.__iterator__):
            row = []

        if row and self.search_regex \
                and not any([el for el in row
                             if self.search_regex.search(el)]):
            row = []

        if row and self.search_string \
                and not any([el for el in row
                             if str(el).find(self.search_string) != -1]):
            row = []

        if row and self.column_regex and not self.__check_column_regex__(row):
            row = []

        if row and self.columns:
            ind_lst = self.__transform_indexes__(self.columns, len(self._fieldnames))
            row = [val for key, val in enumerate(row) if key + 1 in ind_lst]

        return row

    def __next_list__(self):
        if self.line_num == 0:
            # Used only for its side effect.
            # noinspection PyStatementEffect
            self.fieldnames
        row = next(self.reader)
        self.line_num = self.reader.line_num

        # unlike the basic reader, we prefer not to return blanks,
        # because we will typically wind up with a dict full of None
        # values
        while not row:
            row = next(self.reader)
        r = row.copy()
        lf = len(self.fieldnames)
        lr = len(row)
        if lf > lr:
            for _ in self.fieldnames[lr:]:
                r.append(self.restval)

        return r


class _readerXSV:

    def __init__(self, fp, dialect='excel', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL):
        self.fp = fp
        self.dialect = dialect
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.quoting = quoting
        self.line_num = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            line = self.fp.readline()
            self.line_num += 1
        except (UnicodeDecodeError, UnicodeError):
            raise csv.Error(f'Error reading line {self.line_num}') from None

        if not line:
            return None

        line = line.rstrip('\n')

        if self.quoting == csv.QUOTE_NONE:
            yield [s for s in line.split(self.delimiter)]

        elif self.quoting == csv.QUOTE_MINIMAL:
            chunks = []
            in_quote = False
            for c in line:
                if in_quote:
                    if c == self.quotechar:
                        in_quote = False
                    else:
                        chunks.append(c)
                elif c == self.quotechar:
                    in_quote = True
                else:
                    if c == self.delimiter:
                        yield chunks
                        chunks = []
                    else:
                        chunks.append(c)

        else:
            raise ValueError(f'Invalid quoting mode {self.quoting}')


# class ParsedFile:
#     class QuotingTypes:
#         pass
#
#     def __init__(self, io: TextIO, delimiter: str = ',', has_header: bool = True,
#                  force_parse: bool = False, quoting: int = 0):
#         self._io = io
#
#         logger.debug(f'Start parsing IO with {"" if has_header else "no"} header,'
#                      f'delimiter is {delimiter}, with quoting level {quoting}'
#                      f'and {"" if force_parse else "no"} forcibly process an ill-formed format input.')
#
#         self._read_io(io, delimiter, has_header, quoting)
#
#         # row_col_num = {len(row) for row in self._data} | \
#         #               {len(self._header), } if self._header and len(self._header) else {}
#         # if len(row_col_num) > 1 and not force_parse:
#         #     raise Exception(f'An ill-formed format input. Different amount of columns {row_col_num}.')
#
#         # if self._header:
#         #     logger.debug(f'Input data has the following header: {self._header}.'
#         #                  f'Header column number is {len(self._header)}')
#
#         # if len(row_col_num) > 1:
#         #     logger.debug(f'An ill-formed format input. Different amount of columns {row_col_num}.')
#
#         # self._data = [  # Transform the list of rows of list of values to list of rows of dict
#         #     {
#         #         self._header[ind] if self._header and ind < len(self._header) else ind: row_col_num
#         #         for ind, row_col_val in enumerate(row)
#         #     }
#         #     for row in self._data
#         # ]
#
#     def _read_io(self, io: TextIO, delimiter: str = ',', has_header: bool = True, quoting: int = 0) -> None:
#         try:
#             self._data = list(csv.DictReader(io, delimiter=delimiter, quoting=quoting,
#                                              **{
#                                                  **({'fieldnames': None,
#                                                      'default': lambda ind: str(ind),
#                                                      } if not has_header else {}),
#                                              }))
#
#             logger.info(f'{len(self._data)} lines was read from the input.')
#         except Exception as e:
#             logger.error(f'An error occurred while reading input during parsing: {e}')
#             raise


def xsv_reader(io, dialect='excel', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, pure: bool = False):
    """
    Read a CSV file.

    fp: a file object
    dialect: the dialect to use, defaults to 'excel'
    delimiter: the delimiter to use, defaults to ','
    quotechar: the quote character to use, defaults to '"'
    quoting: the quoting method to use, defaults to QUOTE_MINIMAL

    """

    if io is None:
        raise TypeError('fp must be a file object')

    reader = _readerXSV(io, dialect, delimiter, quotechar, quoting)
    try:
        for row in reader:
            yield row
    finally:
        reader.close()


def set_log_level(level: int) -> None:
    # match level:
    #     case 1:
    #         console_handler.setLevel(logging.WARNING)
    #         logger.setLevel(logging.WARNING)
    #     case 2:
    #         console_handler.setLevel(logging.INFO)
    #         logger.setLevel(logging.INFO)
    #     case v if v >= 3:
    #         console_handler.setLevel(logging.DEBUG)
    #         logger.setLevel(logging.DEBUG)
    if level == 1:
        console_handler.setLevel(logging.WARNING)
        logger.setLevel(logging.WARNING)
    elif level == 2:
        console_handler.setLevel(logging.INFO)
        logger.setLevel(logging.INFO)
    elif level >= 3:
        console_handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)


def packet_version() -> str:
    return __version__
