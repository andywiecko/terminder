#!/bin/python

from config import *

def split_substr(String,x=10): 
    string = String.decode('utf8')
    L = len(string) // x
    P = len(string) % x
    ret = []
    for i in range(L):
        ret.append(string[0+i*x:x+i*x])
    if P != 0: ret.append(string[-P:])
    return ret

def print_line():
    print LINE_WIDTH*LINE_SYMB

def print_header():
	print_line()
	print " INCOMING EVENTS IN THE NEXT %i WEEKS:" % WEEKS_DEPTH
	print_line()
