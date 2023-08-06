import datetime

from ._ConsoleColors import ConsoleColors
from ._util import *
from .logPPPLevel import logPPPLevel

__all__ = ['__version__', 'IS_COLOR', 'LEVEL', 'logPPPLevel', 'info', 'warning', 'error', 'debug', 'critical']
__version__ = '1.1.0'

# 是否开启颜色
IS_COLOR = True
# 等级
LEVEL = logPPPLevel.INFO


# 日志输出
def _base(args, sep=' ', end='\n', file=None, _level=logPPPLevel.INFO, color=ConsoleColors.RESET, is_color=True):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    args = "{:<20} {:<8} {}  {}".format(timestamp, get_caller_file_basename_path(), _level['name'], args)
    if is_color is None and IS_COLOR or is_color is True:
        args = f"{color}{args}{ConsoleColors.RESET}"
    if _level['level'] >= LEVEL['level']:
        print(args, sep=sep, end=end, file=file)


# info等级
def info(args, sep=' ', end='\n', file=None, is_color=None):
    _base(args, sep, end, file, logPPPLevel.INFO, ConsoleColors.RESET, is_color)


# warning等级
def warning(args, sep=' ', end='\n', file=None, is_color=None):
    _base(args, sep, end, file, logPPPLevel.WARNING, ConsoleColors.YELLOW, is_color)


# error等级
def error(args, sep=' ', end='\n', file=None, is_color=None):
    _base(args, sep, end, file, logPPPLevel.ERROR, ConsoleColors.RED, is_color)


# debug等级
def debug(args, sep=' ', end='\n', file=None, is_color=None):
    _base(args, sep, end, file, logPPPLevel.DEBUG, ConsoleColors.RED, is_color)


# critical等级
def critical(args, sep=' ', end='\n', file=None, is_color=None):
    _base(args, sep, end, file, logPPPLevel.CRITICAL, ConsoleColors.RED, is_color)
