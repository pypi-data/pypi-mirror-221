# -*- coding: utf-8 -*-
from __future__ import print_function

import datetime
import logging
import pprint
import sys
from itertools import islice
from urllib.parse import parse_qs

import webuntis
from alt_credentials_HTL_HOR import credentials

OFFSET_DAYS = -50 # test in future/back in time

# Example: context manager + show how to access most of the data
#

# ***DO NOT USE THIS EXAMPLE AS-IS***
# Properties that are printed here may contain arbitrary
# *unescaped* HTML. That is not expected, but you should not trust
# input from remote sources in general.


#logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

today = datetime.date.today() + datetime.timedelta(days=OFFSET_DAYS)
oneweek = today + datetime.timedelta(days=7)
monthago = today - datetime.timedelta(days=30)

monday = today - datetime.timedelta(days=today.weekday())
friday = monday + datetime.timedelta(days=4)

sampleQR="untis://setschool?url=urania.webuntis.com&school=htl3r&user=HOR&key=ZXZJLM5J3YBONH5V&schoolNumber=7088200"

p = parse_qs(sampleQR)

#with webuntis.Session(**credentials, use_cache=True).login() as s:
with webuntis.Session(**credentials).login() as s:

    st = s.statusdata()
    print("statusdata", st, repr(st))

    print("last import", s.last_import_time(), s.last_import_time().date, sep=" | ")

    # andi = s.get_student(surname="Arthofer", fore_name="Patrick")
    # hor = s.get_teacher(surname="Hörandl", fore_name="August")
    # print(andi)
    # print(hor)


    hol = s.teachers().filter(name='HOR')[0]
    print(hol)
    tableRaw = s.timetable_extended(teacher=hol, start=monday, end=friday)
    tableRawC = tableRaw.combine()

    p = tableRaw[0]
    print("data", p._data)
    print()

    try:
        for reg in s.class_reg_events(start=monthago, end=today):
            print(reg.category)
    except webuntis.errors.RemoteError:
        print("FAILED: class_reg_events")

    rooms = s.rooms()
    rid = [r.id for r in rooms ]
    rid.sort()
    print(tableRawC)

    print("tableRawC[0]", repr(tableRawC[0]))

    klassen = s.klassen()
    k = klassen.filter(name="4CN")[0]
    print(k, k.teacher1, k.teacher2)

    if 1:
        for st in islice(s.students(), 1, 10):
          try:
            print("student", st, st.full_name, repr(st), sep=" | ")

            #table = s.timetable(student=st, start=monday, end=friday)
            #tableExt = s.timetable_extended(student=st, start=monday, end=friday)
          except  UnicodeEncodeError:
              pass

    if 1:
        for t in islice(s.teachers(), 10):
            print("teacher", t, t.full_name, repr(t), sep=" | ")

        for k in islice(s.klassen(), 10):
            print("klasse", k, k.long_name, repr(k), sep=" | ")

        for r in islice(s.rooms(), 10):
            print("room", r, r.long_name, repr(r), sep=" | ")

        for d in s.departments():
            print("department", d, d.long_name, repr(d), sep=" | ")

        for h in s.holidays():
          try:
            print("holidays", h, h.short_name, repr(h), sep=" | ")
          except  UnicodeEncodeError:
              pass

        for sj in s.schoolyears():
            print("schoolyears", sj, sj.name, repr(sj), sep=" | ")

        for subj in islice(s.subjects(), 10):
            print("subjects", subj, subj.long_name, repr(subj), sep=" | ")

        for tg in islice(s.timegrid_units(), 10):
            print("timegridunit", tg, repr(tg), sep=" | ")


        try:
            for ext in s.exam_types():
                print("ext", ext, " | ", repr(ext))
        except webuntis.errors.RemoteError as e:
            print("\n\nfailed to get exam types:", e)
        except  UnicodeEncodeError:
              pass

        try:
            for ex in s.exams(start=today, end=oneweek, exam_type_id=1):
                print("exam", ex," | ", repr(ex))
                print("     when:", ex.start, " bis ", ex.end)
                print("       te:", ex.teachers)
                print("          ", ex.teachers[0].full_name)
                print("       su:", ex.subject)
                print("     stud:", ex.students)
                print("  klassen:", ex.klassen)
                if ex.students:
                    print("        ", ex.students[0].long_name)

        except webuntis.errors.RemoteError as e:
            print("\n\nfailed to get exams:", e)

        substitutions = s.substitutions(start=monday, end=friday)
        short_subst = substitutions.combine()

        for subst in islice(short_subst, 10):
            print("subst", subst, sep=" | ")
        for subst in islice(short_subst, 3):
            print("subst details:")
            print("   type:", subst.type)
            print("   teachers:", ", ".join(t.name for t in subst.teachers))
            print("   subj:", ", ".join(s.name for s in subst.subjects))
            print("   kl:", ", ".join(k.name for k in subst.klassen))
            print("   when:", subst.start, " bis ", subst.end)

        print("timetable_with_absences")
        try:
            for ab in islice(s.timetable_with_absences(start=today, end=oneweek), 1, 100, 20):
                print("abs:", ab.start, " -- ", ab.end, "|", repr(ab))

        except webuntis.errors.RemoteError as e:
            print("\n\nfailed to get timetable_with_absences:", e)

        print("class_reg_events")
        try:
            crel = s.class_reg_events(start=today, end=oneweek)
            for cre in crel:
                print("class reg event:", cre.student, cre.student.long_name, cre.date, cre.reason, cre.text,
                      repr(cre), sep=" | ")
        except webuntis.errors.RemoteError as e:
            print("\n\nfailed to get class_reg_events:", e)

        print("class_reg_category_groups")
        try:
            crcgl = s.class_reg_category_groups()
            for crcg in crcgl:
                print("class reg category_group:", crcg.name, repr(crcg), sep=" | ")
        except webuntis.errors.RemoteError as e:
            print("\n\nfailed to get reg_category_groups:", e)

        print("class_reg_categories")
        try:
            crcl = s.class_reg_categories()
            for crc in crcl:
                print("class reg category", crc.group, crc.longname, repr(crc), sep=" | ")
        except webuntis.errors.RemoteError as e:
            print("\n\nfailed to get class_reg_categories:", e)

        # ------------------------------------------------------------------------------------------

        klasse = s.klassen()[1]
        # tableRaw = s.timetable(klasse=klasse, start=monday, end=friday)
        tableRaw = s.timetable_extended(klasse=klasse, start=monday, end=friday)

        tableRawC = tableRaw.combine()

        print("Raw", len(tableRaw))
        pprint.pprint(list(tableRaw)[:20])
        print("Combined", len(tableRawC))
        pprint.pprint(list(tableRawC)[:20])

        table = tableRaw.to_table()

        print()
        print()
        print('<h1>', klasse.name, '</h1>')
        print('<table border="1"><thead><th>Time</th>')
        for weekday in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
            print('<th>' + str(weekday) + '</th>')

        print('</thead><tbody>')
        for time, row in table:
            print('<tr>')
            print('<td>{}</td>'.format(time.strftime('%H:%M')))
            for date, cell in row:
                print('<td>')
                for period in cell:
                    print(', '.join(su.name for su in period.subjects))
                    c =  period.code_color

                print('</td>')

            print('</tr>')
            break

        print('</tbody></table>')


