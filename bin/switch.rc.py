#!/usr/bin/env python

# switch.rc.py
# '20-07-22-Wed.    Ver. 0.1
# Nakazato T.

import sys
import csv

if __name__ == '__main__':

    if argv:
        path = sys.argv[1]

        f = open(path)
    else:
        f = sys.stdin
        
    for line in csv.reader(f, dialect="Excel-tab"):

