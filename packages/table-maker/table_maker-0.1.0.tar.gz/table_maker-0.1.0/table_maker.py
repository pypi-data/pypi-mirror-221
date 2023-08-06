"""Create strings with carriage returns, that when printed or written resemble a table. 
This module also includes some utilities for working with these table strings.
This only works for tables with more than one dimension/column.
"""
from typing import List, Union, Tuple, Set, Dict, Any
from itertools import zip_longest
from re import search

Seq = Union[List[str], Tuple[str], Set[str]]

def make_table(cols: Seq,
               rows: Seq,
               scaling: float=1.5,
               sort_col: int=0,
               reverse: bool=False) -> str:
    """Make a formatted table with left justified text. 

    Parameters
    ----------
    cols: a sequence of column names
    rows: a nested sequence of data, such as: (('outside', 'hot'), ('inside', 'cold'))
    sort_col: the index position of the column on which to sort the table, defaults to zero
    scaling: the scaling factor to apply to the table to ensure the contents fit

    Example
    -------
    >>> cols = ('dist. (ft)', 'contested?', 'result')
    >>> rows = (('15', 'yes', 'miss'), ('27', 'no', 'miss'), ('03', 'no', 'make'))
    >>> table=make_table(cols, rows, scaling=3)
    >>> print(table)
    +------------+------------+------------+
    | dist. (ft) | contested? | result     |
    +============+============+============+
    | 03         | no         | make       |
    +------------+------------+------------+
    | 15         | yes        | miss       |
    +------------+------------+------------+
    | 27         | no         | miss       |
    +------------+------------+------------+
    """
    scale = max(scaling, 1.2)
    dist = round(max(map(len, (r for row in rows for r in row))) * scale)
    sep = ('+' + ('-' * dist)) * len(cols) + '+'
    parts = ['| ' + col for col in cols]
    header = ''.join((pt + (' ' * (1 + dist - len(pt))) for pt in parts)) + '|'
    cells = []
    for row in sorted(rows, reverse=reverse, key=lambda x: x[sort_col].lower()): 
        pts = ['| ' + r for r in row]
        cells.append(''.join((pt + (' ' * (1 + dist - len(pt))) for pt in pts)) + '|')
        cells.append(sep)
    return '\n'.join((sep, header, sep.replace('-', '='), *cells))

# listed below are some utilities for the `table` string created above 

def head(table: str, n: int=3) -> str:
    """Output a table that only contains the first n rows of
    the input table"""
    return '\n'.join(table.split('\n')[:3+n*2])

def tail(table: str, n: int=3) -> str:
    """Output a table that only contains the last n rows of
    the input table"""
    return '\n'.join((get_header(table), *get_rows(table).split('\n')[-n*2:]))

def length(table: str) -> int:
    """Get table length"""
    return len(table.split('\n')[3:][0::2])

def insert_row_numbers(table: str) -> str:
    """Place row numbers to the left of the table string.

    Example
    -------
    >>> cols = ('dist. (ft)', 'contested?', 'result')
    >>> rows = (('15', 'yes', 'miss'), ('27', 'no', 'miss'), ('03', 'no', 'make'))
    >>> table=make_table(cols, rows, scaling=3)
    >>> table_with_row_numbers = insert_row_numbers(table)
    >>> print(table_with_row_numbers)
       +------------+------------+------------+
       | dist. (ft) | contested? | result     |
       +============+============+============+
    1  | 03         | no         | make       |
       +------------+------------+------------+
    2  | 15         | yes        | miss       |
       +------------+------------+------------+
    3  | 27         | no         | miss       |
       +------------+------------+------------+
    """
    splits = table.split('\n')
    rows = ['  ' + split for split in splits[3::2]]
    seps = ['   ' + split for split in splits[4::2]]
    header = ['   ' + split for split in splits[0:3]]
    indices = [str(idx + 1) for idx, _ in enumerate(rows)]
    new_rows = [row[0] + row[1] for row in zip(indices, rows)]
    ret = [row for line in zip(new_rows, seps) for row in line]
    return '\n'.join((*header, *ret))

def insert_title(title: str, table: str) -> str:
    return '\n'.join((title.upper(),table))

def get_header(table: str) -> str:
    return '\n'.join(table.split('\n')[:3])

def get_rows(table: str) -> str:
    return '\n'.join(table.split('\n')[3:])

def maybe_table(table: str) -> bool:
    """An inexact approach to check if a string is a table"""
    chars = ("+=", "+-", "=+", "-+", "|\n", "-+\n", "=+\n")
    return all(([ch in table for ch in chars], search('\|\s\w', table)))

def chop(table: str) -> str:
    """Split a table in half"""
    ln = length(table)
    size = (ln, ln + 1)[ln % 2 != 0]
    h = get_header(table)
    rows = get_rows(table).split('\n')
    return '\n'.join((h, *rows[:size], '\n', h, *rows[size:]))

def deconstruct(table: str) -> Tuple[List[str], List[Tuple[Union[str, Any], ...]]]: 
    """Extract the rows and columns from a table string"""
    cols = get_header(table).split('\n')[1].replace('|', '').split()
    items = [val for val in '\n'.join(get_rows(table).split('\n')[::2]).split('|') if val not in ('', '\n')]
    rows = [tuple(row) for row in zip_longest(*[iter([item.replace(' ', '') for item in items])]*len(cols))]
    return cols, rows

def transform(table: str) -> Dict[str, List[str]]:
    """Convert a table string into a dictionary, where
    the columns are the keys and the values are lists of the rows"""
    cols, rows = deconstruct(table)
    return {cols[i]: [row[i] for row in rows] for i in range(len(cols))}

def capitalize_inputs(cols: Seq, rows: Seq): 
    """
    Formatting tool -- capitalize the rows and column names. 

    Example
    ------
    >>> cols = ('navy', 'ship name', 'class')
    >>> rows = (
       ('royal navy', 'exeter', 'exeter'), 
       ('royal navy', 'ajax', 'leander'), 
       ('royal navy', 'achilles', 'leander'),
       ('kriegsmarine', 'admiral graf spee', 'deutschland'))
    >>> x, y = capitalize_inputs(cols, rows)
    >>> print(make_table(cols=x, rows=y, scaling=1.25, reverse=True))
    +---------------------+---------------------+---------------------+
    | Navy                | Ship Name           | Class               |
    +=====================+=====================+=====================+
    | Royal Navy          | Exeter              | Exeter              |
    +---------------------+---------------------+---------------------+
    | Royal Navy          | Ajax                | Leander             |
    +---------------------+---------------------+---------------------+
    | Royal Navy          | Achilles            | Leander             |
    +---------------------+---------------------+---------------------+
    | Kriegsmarine        | Admiral Graf Spee   | Deutschland         |
    +---------------------+---------------------+---------------------+
    """
    out_rows = [tuple(row) for row in 
                zip_longest(*[iter([r.title() for row in rows for r in row])]*len(cols))]
    out_cols = tuple((col.title() for col in cols))
    return out_cols, out_rows

def remove_seps(table: str) -> str: 
    """
    Convert a table like this: 
    +------+------+
    | item1| item2|
    +======+======+
    | a    | z    |
    +------+------+
    | b    | y    |
    +------+------+
    | c    | x    |
    +------+------+

    ...into this: 
    +------+------+
    | item1| item2|
    +======+======+
    | a    | z    |
    | b    | y    |
    | c    | x    |
    +------+------+
    """
    rows = get_rows(table).split('\n')[::2]
    header = get_header(table).split('\n')
    return '\n'.join((*header, *rows, header[0]))
