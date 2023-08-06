# -*- coding: utf-8 -*-
from __future__ import print_function

import datetime
import logging
import pprint
import sys
from itertools import islice

import webuntis
from alt_credentials_HTL2 import credentials


#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

with webuntis.Session(**credentials).login() as s:

    monday = s.schoolyears().current.end - datetime.timedelta(days=10) - datetime.timedelta(days=datetime.date.today().weekday())
    #monday = datetime.date.today() - datetime.timedelta(days=datetime.date.today().weekday())

    while monday < s.schoolyears().current.end: # Wrapping loop
        friday = monday + datetime.timedelta(days=4)
        print(monday, friday)
        try:
            tt = s.timetable(klasse=s.klassen().filter(name="3AI")[0], start=monday, end=friday)
        except webuntis.errors.DateNotAllowed: # Error Message is output anyway
            print("OK")
            break
        # .. Code that interacts with the timetable

        monday += datetime.timedelta(days=7)
