import logging
import pprint
from datetime import datetime, timedelta

import webuntis
from alt_credentials_HTL2 import credentials

#logging.basicConfig(level=logging.DEBUG)

print(f"User: {credentials['username']}")

with webuntis.Session(**credentials).login() as sess:

    yearstart = sess.schoolyears().current.start.date()
    print(f"Schoolyear: {yearstart}")

    start = datetime.fromisoformat("2018-12-20")
    klasse = sess.klassen().filter(name="1BI")[0]
    tableRaw = sess.timetable(klasse=klasse, start=start, end=start)

    tableRawC = tableRaw.combine()

    print("Raw", len(tableRaw))
    for p in tableRaw:
        print(p.start, p.end, p.subjects, p.teachers)
    print("Combined", len(tableRawC))
    for p in tableRawC:
        print(p.start, p.end, p.subjects, p.teachers)


