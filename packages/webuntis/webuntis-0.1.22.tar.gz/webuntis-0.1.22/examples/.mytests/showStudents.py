import logging

import webuntis
from alt_credentials_HTL_himmler import credentials

#logging.basicConfig(level=logging.DEBUG)

print(f"User: {credentials['username']}")

with webuntis.Session(**credentials).login() as sess:
    yearstart = sess.schoolyears().current.start.date()
    print(f"Schoolyear: {yearstart}")

    students = sess.students()
    print(f"Number of studens: {len(students)}")
    for i, student in zip(range(15), students):
        print(f"{i:3}: {student}")

