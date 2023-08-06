"""
Utilities and convenience functions for using the Python standard library.
"""
import re
import os
import sys
import sqlite3
import datetime
import contextlib
import tempfile
import logging
from typing import Any, List, Tuple, Union, TextIO, BinaryIO
from collections.abc import Sequence, Generator


def all_except(seq: Sequence[Any], omissions: Sequence[Any]) -> List[Any]:
    """All entries of a list except the one mentioned in `omissions`.

    Args:
        seq (seq): sequence of objects
        omissions (seq): sequence of omissions
    Returns:
        list of remaining objects
    """
    omissions = set(omissions)
    return [entry for entry in seq if entry not in omissions]


def isstring(s: Any) -> bool:
    """Is the argument a string?

    Args:
        s: object
    Returns:
        bool: whether it is of type `str` or `bytes`
    """
    return isinstance(s, (str, bytes))


def if_true(flag: bool, value: Any, default: str = '') -> Any:
    """If the flag is true, return the value, otherwise the default.

    Args:
        flag (bool): control flag
        value (object): value to return if the flag is true
        default (object): value to return if the flag is false
    Returns:
        the chosen value as specified above
    """
    if flag:
        return value
    else:
        return default


def wi_perc(value: float, reference: float) -> Tuple[float, float]:
    """Return the value and the percentage of the value in the reference.

    Args:
        value (number): value to compare
        reference (number): total amount
    Returns:
        value, perc: The original value and the percentage (scaled to 100)
    """
    return value, value / reference * 100.


def perc_str(value: float, reference: float) -> str:
    """Return a string with the value and the percentage of the value in
    the reference.

    Args:
        value (number): value to compare
        reference (number): total amount
    Returns:
        str: value with percentage
    """
    _, perc = wi_perc(value, reference)
    return f"{value} ({perc:.2f} %)"


def first_of_each_item(items: Sequence[Any]) -> List[Any]:
    """The first subitem of each item in the input

    Args:
        items (sequence of indexable objects): input list of items
    Returns:
        list of objects: For each item in the input, `item[0]`.
    """
    return [item[0] for item in items]


def makedir_unless_exists(dirpath: str) -> None:
    """Create a directory path unless it already exists.

    Args:
        dirpath (str): directory path
    """
    if not os.path.isdir(dirpath):
        os.makedirs(dirpath)


def make_path_relative_to(filepath: str, reference_path: str) -> str:
    """Make a filepath relative to a given reference path.

    This is needed for HTML links to images, for example.

    Args:
        filepath (str): input filepath
        reference_path (str): reference filepath
    Returns:
        str: relative filepath as seen from the reference filepath
    """
    parts = os.path.normpath(filepath).split(os.path.sep)
    parts_ref = os.path.normpath(reference_path).split(os.path.sep)
    n_ref = len(parts_ref)
    i = 0
    for i, part in enumerate(parts):
        if i >= n_ref or part != parts_ref[i]:
            break
    return os.path.join(*(['..'] * (n_ref - i) + parts[i:]))


def filepath_in_dir_of(filename: str, filepath_in_same_dir: str) -> str:
    """Take the directory of the given filepath and add the given filename to
    it.

    Args:
        filename: a filename for the directory
        filepath_in_same_dir: a filepath defining the directory
    Returns:
        composed filepath
    """
    return os.path.join(os.path.dirname(filepath_in_same_dir), filename)


@contextlib.contextmanager
def redirect_stdouterr(outfp: TextIO, errfp: TextIO) -> Generator[None]:
    """Context manager for temporary redirection of `sys.stdout` and
    `sys.stderr`.

    Args:
        outfp (output stream): output stream to redirect the standard output
            stream to (default=`os.devnull`)
        errfp (output stream): path or output stream to redirect
            the standard error stream to (default=`os.devnull`)

    If you want to keep one of the two unchanged, just pass `sys.stdout` or
    `sys.stderr`, respectively.
    """
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    try:
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout = outfp
        sys.stderr = errfp
        yield
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr


class BranchedOutputStreams:
    """Output stream that delegates to multiple other output streams

    Args:
        streams (seq of output streams): output streams to delegate to
    """
    def __init__(self, streams: Sequence[TextIO]):
        self.streams = streams

    def write(self, message: str) -> None:
        """Write a message to all output streams.

        Args:
            message (str): message to write
        """
        for stream in self.streams:
            stream.write(message)

    def flush(self) -> None:
        """Flush all output streams."""
        for stream in self.streams:
            stream.flush()

    def close(self) -> None:
        """Close all output streams."""
        for stream in self.streams:
            stream.close()


@contextlib.contextmanager
def open_overwriting_safely(
        filepath: str, mode: int
) -> Generator[Union[TextIO, BinaryIO]]:
    """Open a temporary file and rename it in the end.

    Instead of overwriting the given file directly, open a temporary file
    in the same directory, write into it and rename the temporary file to the
    given filepath in the end.

    This way, if an exception occurs, the original file contents is preserved.

    Args:
        filepath (str): filepath to create / overwrite in the end
        mode (int): See `tempfile.NamedTemporaryFile`.
    """
    filepath_tmp = None
    try:
        with tempfile.NamedTemporaryFile(
            mode=mode, delete=False, dir=os.path.dirname(filepath)
        ) as fout:
            filepath_tmp = fout.name
            yield fout
        os.rename(filepath_tmp, filepath)
        filepath_tmp = None
    finally:
        if filepath_tmp is not None and os.path.exists(filepath_tmp):
            os.remove(filepath_tmp)


def ansiicol(color_num: int, is_bright: bool = False) -> str:
    """ANSI escape code for the given color number
    https://en.wikipedia.org/wiki/ANSI_escape_code

    Args:
        color_num (int): color number
        is_bold (bool): whether to use bold face
    Returns:
        ANSII escape code
    """
    if is_bright:
        bright_part = ';1'
    else:
        bright_part = ''
    return f"\x1b[{color_num}{bright_part}m"


TERMSEQ = {
    'red[': ansiicol(31),
    'br_red[': ansiicol(31, True),
    'green[': ansiicol(32),
    'br_green[': ansiicol(32, True),
    'yellow[': ansiicol(33),
    'br_yellow[': ansiicol(33, True),
    'cyan[': ansiicol(36),
    'br_cyan[': ansiicol(36, True),
    'blue[': ansiicol(34),
    'br_blue[': ansiicol(34, True),
    #'bold[': "\x1b[30;1m",
    ']': "\x1b[0m",
}


@contextlib.contextmanager
def sqlite3_conn(filepath) -> Generator[Tuple[sqlite3.Connection, sqlite3.Cursor]]:
    """Context manager for a connection to a Sqlite3 database file

    Args:
        filepath (str): filepath to the database file
    Yielding:
        db, cursor; the database connection and the cursor
    """
    db = None
    cursor = None
    try:
        db = sqlite3.connect(filepath)
        cursor = db.cursor()
        yield db, cursor
    finally:
        if cursor is not None:
            cursor.close()
        if db is not None:
            db.close()


SECONDS_IN_HOUR = 3600

SECONDS_IN_DAY = 24 * SECONDS_IN_HOUR


def n_days_ago(n_days: int) -> datetime.datetime:
    """The datetime object for the day n_days days ago

    Args:
        n_days (int): number of days to go into the past
    Returns:
        `datetime.datetime`: datetime object for that day in the past
    """
    return datetime.date.today() - datetime.timedelta(n_days)


def n_days_from_today(n_days: int) -> datetime.datetime:
    """The datetime object for the day n_days from today

    Args:
        n_days (int): number of days to go into the future
    Returns:
        `datetime.datetime`: datetime object for that day in the future
    """
    return datetime.date.today() + datetime.timedelta(n_days)


def today_isoformat() -> str:
    """Today in ISO date format

    Returns:
        str: in ISO date format
    """
    return datetime.date.today().isoformat()


def create_console_logger(module: str, level: int = logging.DEBUG) -> logging.Logger:
    """Create a default console logger for a given module.

    Args:
        module (str): module name
        level (int): logging level
    Returns:
        `logging.Logger`
    """
    logger = logging.getLogger(module)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s"))
    logger.addHandler(handler)

    return logger


def strip_margin(text: str) -> str:
    """After each newline in the string, strip the whitespace part before a
    vertical bar just like in Scala.

    Args:
        text: input string
    Returns:
        output string
    """
    return re.sub('\n[ \t]*[|]', '\n', text)
