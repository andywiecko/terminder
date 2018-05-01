#!/bin/python

from config import *
from libs.misc import print_header
from libs.misc import print_line
from libs.misc import split_substr

from datetime import datetime

now = datetime.now()

def time_to_now(event_date):
    return event_date - now

def next_reg_event(date):
    temp_year = now.year
    event_date = datetime(temp_year,date.month,date.day)
    if date.month == now.month and date.day == now.day:
        return event_date
    while time_to_now(event_date).days < 0:
        temp_year += 1
        event_date = datetime(temp_year,date.month,date.day)
    return event_date


# reg: regular or not regular events
class Event:
	def __init__(self,text,date,reg=1):
		self.text = text
		self.date = date
                self.reg  = reg

	def __lt__(self, other):
		event_date = self.date
                other_date = other.date
                if self.reg == 1:
                    event_date = next_reg_event(self.date)
                if other.reg == 1:
                    other_date = next_reg_event(other.date)
           
		return event_date < other_date

	def __repr__(self):
		return self.text+'|'+str(self.date)

	def __str__(self):
		return self.text+'|'+str(self.date)

        def full_info(self):
                print '\033[34m',
 	        TEXT = self.text 
	        if len(TEXT) > MAX_TEXT_WIDTH:
	            TEXT_M = split_substr(TEXT,MAX_TEXT_WIDTH)
	            for j in TEXT_M[:-1]:
	                print j
	            print TEXT_M[-1],
	            print (MAX_TEXT_WIDTH-len(TEXT_M[-1]))*' ',
	        else: 
	            print self.text,
	            print (MAX_TEXT_WIDTH-len(self.text.decode('utf8')))*' ',
                print '\033[33m',

def open_regular_events(path):
    lines = open(path,'r').readlines()
    records = "".join("".join("".join(lines).split("\n")).split("{")[1:]).split("}")[:-1]
    for i in records:
        rec = i.split(',')
        date = "".join(rec[1].split()).split('/')
        month = int(date[0])
        day = int(date[1])
        EVENTS.append(Event(rec[0],datetime(1,month,day)))

def open_nonregular_events(path):
    lines = open(path,'r').readlines()
    records = "".join("".join("".join(lines).split("\n")).split("{")[1:]).split("}")[:-1]
    for i in records:
        rec = i.split(',')
        date = "".join(rec[1].split()).split('/')
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])
        EVENTS.append(Event(rec[0],datetime(year,month,day),0))


def output():
	NZE = 0 # number of incoming events
	for i in EVENTS:

            if i.reg == 1: event_date = next_reg_event(i.date)
            else: event_date = i.date
            
            diff = time_to_now(event_date).days
            hour = time_to_now(event_date).seconds//3600
            minute = (time_to_now(event_date).seconds//60)%60
	    if -1 <= diff < WEEKS_DEPTH * 7:
                i.full_info()
	        print 'at',str(now.year)+'/'+str(i.date.month)+'/'+str(i.date.day), 
	        if diff >= 0: print "(up to\033[32m",diff,"days\033[33m",hour, "h",minute,"m)"
                if diff < 0: print '\033[7mTODAY!\033[0m\033[33m'
	        NZE += 1
	    
            else:
                pass
                #break

	if NZE == 0:
	    print " None"

def incoming_events():
    print '\033[33m\r',
    print_header()
    EVENTS.sort()
    output()
    print_line()


