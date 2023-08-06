import sys
from pprint import pprint

from alt_credentials_HTL import credentials
import datetime
import logging
import webuntis

logging.basicConfig(level=logging.DEBUG)

start = datetime.date.fromisoformat(sys.argv[1])

logging.info(f"{start = }")

tt = dict()

with webuntis.Session(**credentials).login() as s:
    teachers = s.teachers()
    for teacher in teachers:
        logging.info(f"{teacher = }")
        tableRaw = s.timetable_extended(teacher=teacher, start=start, end=start)

        for p in tableRaw:
            for t in p.teachers:
                if t not in tt:
                    tt[t] = (p.start, p.end)
                else:
                    tt[t] = (min(tt[t][0], p.start), max(tt[t][1], p.end))

for t, (frm, to) in sorted(tt.items(), key=lambda k: k[0].name):
    print(f"{t.name}: {frm} -- {to}")
