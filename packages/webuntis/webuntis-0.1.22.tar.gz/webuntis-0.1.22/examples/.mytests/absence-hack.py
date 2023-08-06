import argparse
import datetime
import logging
import sys
from collections import defaultdict, Counter

import webuntis
import webuntis.objects
from alt_credentials_HTL2 import credentials
from log import my_logger


class ListOfAbsences:
    needed_data = [u'studentId', u'date', u'startTime']
    add_data = [u'studentGroup', u'checked', u'absentTime']

    def __init__(self):
        self.all_absences = dict()

    def addEntry(self, a):
        data = a._data
        needed = tuple(data[k] for k in ListOfAbsences.needed_data)
        additional = [a.student_group, a.checked, a.time, data]
        if needed in self.all_absences:
            old = self.all_absences[needed]
            additional[1] &= old[1]
            additional[2] += old[2]
        self.all_absences[needed] = additional

    def get(self):
        for key in sorted(list(self.all_absences.keys())):
            yield (*key, *self.all_absences[key])


def check_absences(num_days, limit):
    with webuntis.Session(**credentials).login() as sess:
        yearstart = sess.schoolyears().current.start.date()
        ende = datetime.date.today()
        start = max(ende - datetime.timedelta(days=num_days), yearstart)

        students = sess.students()  # fill cache
        my_logger.info(f"Students: {len(students)}")
        my_logger.info(f"Interval: {start} - {ende}")
        absences = sess.timetable_with_absences(start=start, end=ende)
        my_logger.info(f"Count: {len(absences)}")

        absence_days = defaultdict(list)
        bad_students = dict()
        stud2class = defaultdict(Counter)
        last_abs = None

        alle = ListOfAbsences()
        for a in absences:
            alle.addEntry(a)

        for a in alle.get():
            stud, date, start, grp, checked, time, data = a
            if time > 0:
                try:
                    cls = grp.split("_")[1]
                    stud2class[stud][cls] += 1
                except (IndexError, AttributeError):
                    pass

                last_abs = start
                if date not in absence_days[stud]:
                    absence_days[stud].append(date)
                    if len(absence_days[stud]) > limit:
                        days = absence_days[stud][:]
                        bad_students[(stud, days[0])] = (days, data)
                        my_logger.debug(f"-> {stud:5}: {days[0]} - {days[-1]} : {len(days)}")
            elif checked:
                if len(absence_days[stud]) > limit:
                    my_logger.debug(f"  cleared {stud:5}: {date} {start}")
                absence_days[stud].clear()

    print(f"--------------------------- {len(bad_students)}")
    for ((sid, date), (days, data)) in bad_students.items():
        try:
            cls = stud2class[sid].most_common(1)[0][0]
        except IndexError:
            cls = '???'
        a = webuntis.objects.AbsenceObject(data, session=sess)
        stud = a.student
        today = "*" if a.start.date() == ende else ""
        print(f"{stud.name:6} {cls} {stud.full_name:30} {days[0]}...{days[-1]} {len(days):3} {today}     {sid}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check Webuntis for long absences".')

    parser.add_argument('--days', '-d', type=int, help='number of days to look back', default=14)
    parser.add_argument('--limit', '-l', '-c', type=int, help='number of consecutive days', default=4)
    parser.add_argument('--verbose', '-v', action='store_true', help='show more info', dest="verbose", default=False)
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    check_absences(args.days, args.limit)
