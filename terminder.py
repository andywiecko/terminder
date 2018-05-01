#!/bin/python

from libs.events import open_regular_events
from libs.events import open_nonregular_events
from libs.events import incoming_events


path1 = 'nonreg_events'
path2 = 'events'

open_nonregular_events(path1)
open_regular_events(path2)

incoming_events()

print

incoming_events(all=True)


