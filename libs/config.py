#!/bin/python
from datetime import datetime

# event text width
MAX_TEXT_WIDTH = 37
# decoration line width
LINE_WIDTH = 79
# decoration line symbol
LINE_SYMB = '='

WEEKS_DEPTH = 2

# bash colors setting
# tips about format can be found here:
# https://misc.flogisoft.com/bash/tip_colors_and_formatting
FORMAT_END =         '\033[0m'   # reset settings 
TODAY_FORMAT =       '\033[7m'   # inverted colors
STANDARD_FORMAT =    '\033[33m'  # orange color
REG_TEXT_FORMAT =    '\033[34m'  # blue color
NONREG_TEXT_FORMAT = '\033[36m'  # cyan color
WARNCOLOR1 =         '\033[32m'  # green color
WARNCOLOR2 =         '\033[31m'  # red color
