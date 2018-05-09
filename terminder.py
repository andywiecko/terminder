#!/bin/python

from libs.events import open_regular_events
from libs.events import open_nonregular_events
from libs.events import incoming_events
import libs.config
import sys

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-a", "--all",default=False,\
        action="store_true", dest="PRINT_ALL",\
        help="print all records from database")
parser.add_option("-w", "--weeks",default=False,\
        action="store", dest="WEEKS",type=int,\
        help="set events weeks depth")

(options, args) = parser.parse_args()

if options.WEEKS>0:
    libs.config.WEEKS_DEPTH = options.WEEKS

path1 = 'nonreg_events'
path2 = 'events'

try: open_nonregular_events(path1)
except: print "terminder error: can't load", path1

try: open_regular_events(path2)
except: print "terminder error: can't load", path2

if options.PRINT_ALL:
    incoming_events(all=True)
else:
    incoming_events()
