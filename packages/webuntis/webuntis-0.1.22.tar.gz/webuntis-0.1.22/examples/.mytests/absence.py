import argparse
import datetime
import logging
import sys
from collections import defaultdict, Counter

import webuntis
from alt_credentials_HTL2 import credentials
from log import my_logger


def check_absences(num_days, limit):
    with webuntis.Session(**credentials).login() as sess:
        yearstart = sess.schoolyears().current.start.date()
        ende = datetime.date.today()
        start = max(ende - datetime.timedelta(days=num_days), yearstart)

        my_logger.info(f"Interval: {start} - {ende}")
        absences = sess.timetable_with_absences(start=start, end=ende)
        my_logger.info(f"Count: {len(absences)}")

        absence_days = defaultdict(list)
        bad_students = dict()
        stud2class = defaultdict(Counter)
        last_abs = None
        for a in absences:
            stud = a.student
            if a.time > 0:
                try:
                    cls = a.student_group.split("_")[1]
                    stud2class[stud][cls] += 1
                except (IndexError, AttributeError):
                    pass
                d = a.start.date()
                last_abs = a.start
                if d not in absence_days[stud]:
                    absence_days[stud].append(d)
                    if len(absence_days[stud]) > limit:
                        days = absence_days[stud][:]
                        bad_students[(stud, days[0])] = days
                        my_logger.debug(f"-> {stud.full_name:20}: {days[0]} - {days[-1]} : {len(days)}")
            elif a.checked:
                if a.start != last_abs:
                    if len(absence_days[stud]) > limit:
                        my_logger.debug(f"  cleared {stud.full_name:20} : {a.start.date()} {a.start.time()}")
                    absence_days[stud].clear()

    print(f"--------------------------- {len(bad_students)}")
    for (stud, _), days in bad_students.items():
        cls = stud2class[stud].most_common(1)[0][0]
        today = "*" if days[-1] == ende else ""
        print(f"{stud.name:6} {cls} {stud.full_name:30} {days[0]}...{days[-1]} {len(days):3} {today}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check Webuntis for long absences".')

    parser.add_argument('--days', '-d', type=int, help='number of days to look back', default=14)
    parser.add_argument('--limit', '-l', '-c', type=int, help='number of consecutive days', default=4)
    parser.add_argument('--verbose', '-v', action='store_true', help='show more info', dest="verbose", default=False)
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    check_absences(args.days, args.limit)
