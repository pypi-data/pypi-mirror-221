#! /usr/bin/env python3

# 3AFI 28.11   PKT.SEM (184)
# 4BM  10.10   SEM.1   (183)


import datetime
import sys
from collections import defaultdict
from contextlib import contextmanager
from typing import Iterator

import webuntis
from log import my_logger
from webuntis.objects import KlassenObject
from webuntis.session import Session

# when to start - n weeks in the future
STARTWEEKSOFFSET = 4

try:
    # noinspection PyUnresolvedReferences
    import secret
except ImportError as ie:
    with open("sample-secret.py", "w") as f:
        f.write("""
# fill out & rename to secret.py
untis_username = "xxx"
untis_passwd = "topSecret"

gmail_sender = "your-email@gmail.com"
gmail_passwd = "your-email-password"

copy_email = gmail_sender
""")
    my_logger.error("Import failed: " + str(ie) + "\nPlease edit `sample-secret.py` and rename to `secret.py`")
    sys.exit(99)


@contextmanager
def webuntis_login() -> Iterator[Session]:
    """ create a session context
    """
    s = webuntis.Session(
        server='https://urania.webuntis.com',
        username=secret.untis_username,
        password=secret.untis_passwd,
        school='htl3r',
        useragent='WebUntis Test'
    )

    try:
        s.login()
    except Exception as ce:
        my_logger.error("Login failed: " + str(ce))
        raise ce

    my_logger.info("Logged in")
    yield s
    s.logout()


y = datetime.date.today().year
YEAR = f"{y % 100}-{y % 100 + 1}"

print("year", YEAR)

klassenliste = defaultdict(set)
gegstliste = defaultdict(set)
raumliste = defaultdict(set)
jgvliste = defaultdict(set)
allejgv = defaultdict(set)

bad = set()

with webuntis_login() as sess:
    start = datetime.date.today() + datetime.timedelta(weeks=STARTWEEKSOFFSET)
    end = sess.schoolyears().current.end
    # end = start +  datetime.timedelta(weeks=12)

    print("from", start, "to", end)
    print(f"# created {datetime.date.today()} / {start}")

    klasse: KlassenObject
    for klasse in sess.klassen():
        print("#", klasse)
        try:
            jgvliste[klasse.name].add(klasse.teacher1.name)
            allejgv[""].add(klasse.teacher1.name)
            jgvliste[klasse.name].add(klasse.teacher2.name)
            allejgv[""].add(klasse.teacher2.name)
        except IndexError:
            pass
        except KeyError:
            pass

        table = sess.timetable(klasse=klasse, start=start, end=end).to_table()
        for time, row in table:
            for date, cell in row:
                for period in cell:
                    if not period.code:
                        try:
                            for teacher in period.teachers:
                                klassenliste[klasse.name].add(teacher.name)
                                for subject in period.subjects:
                                    gegstliste[subject.name].add(teacher.name)
                                for room in period.rooms:
                                    n = room.name.replace(" ", "_").replace(".", "")
                                    n = "".join(c for c in n if c.isalnum() or c == "_")
                                    for r in n.split("_"):
                                        raumliste[r].add(teacher.name)
                        except IndexError as e:
                            if len(period._data['te']) == 1 and str(period._data['te']) not in bad:
                                print("Teacher??:", period._data['te'], period.subjects)
                                bad.add(str(period._data['te']))
                            # 248   20210212 1AM WEPT -- W.319    OSZ
                            # 244   20210209 2AM WEPT -- W.123    AMO
                            # 239   20210210 3AM KOP     E.KU.1   FRH
                            # 210
                            pass

    for t in sess.teachers():
        print("#", t)
        table = sess.timetable(teacher=t, start=start, end=end).to_table()
        for time, row in table:
            for date, cell in row:
                for period in cell:
                    if not period.code:
                        try:
                            for teacher in period.teachers:
                                for subject in period.subjects:
                                    gegstliste[subject.name].add(teacher.name)
                                try:
                                    for room in period.rooms:
                                        n = room.name.replace(" ", "_").replace(".", "")
                                        n = "".join(c for c in n if c.isalnum() or c == "_")
                                        for r in n.split("_"):
                                            raumliste[r].add(teacher.name)
                                except IndexError as e:
                                    if len(period._data['ro']) == 1 and str(period._data['ro']) not in bad:
                                        print("Room??", period._data['ro'], period.subjects)
                                        bad.add(str(period._data['ro']))
                        except IndexError as e:
                            pass

domain = "@htl.rennweg.at"


def liste_email(li):
    return ",".join(e + domain for e in li).lower()


all_groups = []

with open("liste-add.ps1", "w") as fi:
    print(f"# created {datetime.date.today()} / {start}", file=fi)
    for tmpl, _, tmpls, liste in (
            ("Klassenlehrer {} 20" + YEAR, "Klassenlehrer{}" + YEAR, "Klassenlehrer{}", klassenliste),
            ("Lehrer {} 20" + YEAR, "Lehrer{}_" + YEAR, "Lehrer{}", gegstliste),
            ("Lehrer in Raum {} 20" + YEAR, "LehrerInRaum{}_" + YEAR, "LehrerInRaum{}", raumliste),
            ("Jahrgangsvorstand {} 20" + YEAR, "Jahrgangsvorstand{}_20" + YEAR, "Jahrgangsvorstand_{}", jgvliste),
            ("Jahrgangsvorstaende 20" + YEAR, "Jahrgangsvorstaende_20" + YEAR, "Jahrgangsvorstaende_20" + YEAR, allejgv)
    ):
        print(file=fi)
        for k in sorted(liste.keys()):
            viele = sorted(liste[k])
            if viele:
                g = tmpl.format(k.upper())
                all_groups.append(g)
                smtp = tmpls.format(k.upper()) + domain
                print(
                    'New-DistributionGroup -Name "' + g + '" -DisplayName "' + g + '" -PrimarySmtpAddress "' + smtp + '" -type Distribution',
                    file=fi)
                for e in viele:
                    print(' Add-DistributionGroupMember -Identity "' + g + '" -Member ' + e + "@htl.rennweg.at",
                          file=fi)

with open("liste-del.ps1", "w") as fi:
    for g in all_groups:
        print('Remove-DistributionGroup -Identity "' + g + '"', file=fi)
    print('Remove-DistributionGroup -Identity "' + "Jahrgangsvorstaende" + '"', file=fi)
