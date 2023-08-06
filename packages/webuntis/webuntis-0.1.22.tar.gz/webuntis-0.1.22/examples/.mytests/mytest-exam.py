# -*- coding: utf-8 -*-
from __future__ import print_function

import datetime
import logging
import pprint
import sys
from itertools import islice

import webuntis
from alt_credentials_HTL2 import credentials


# Example: context manager + show how to access most of the data
#

# ***DO NOT USE THIS EXAMPLE AS-IS***
# Properties that are printed here may contain arbitrary
# *unescaped* HTML. That is not expected, but you should not trust
# input from remote sources in general.


logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

today = datetime.date.today() - datetime.timedelta(days=100)
oneweek = today + datetime.timedelta(days=7)

monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

#with webuntis.Session(**credentials, use_cache=True).login() as s:
with webuntis.Session(**credentials).login() as s:
    print("logged in")
    #dummy = s.klassen()
    exams = s.exams(start=s.schoolyears().current.start, end=s.schoolyears().current.end)

    try:
        start = s.schoolyears().current.start
        end = s.schoolyears().current.end
        exams = s.exams(start=monday, end=friday)
 #       for ex in s.exams(start=today, end=oneweek, exam_type_id=1):
        for ex in exams:
            print("exam", ex," | ", repr(ex))
            print("cache", s.cache.keys())
            print("  klassen:", ex.klassen)


    except webuntis.errors.RemoteError as e:
        print("\n\nfailed to get exams:", e)

