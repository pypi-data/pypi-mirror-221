import webuntis
import datetime
import config

""" Autor: Miriam Gehbauer
    liest alle notwendigen Daten aus Webuntis aus
"""

s = webuntis.Session(
    server=config.webuntis_servername,
    username=config.webuntis_username,
    password=config.webuntis_password,
    school=config.webuntis_schule,
    useragent='WebUntis auslesen'
).login()


def get_class(year=None):
    """ gibt alle klassen des Schuljahres aus
    """
    if year is None:
        for k in s.klassen():
            yield (k)
    else:
        for k in s.klassen(schoolyear=year):
            yield (k)


def get_klasse(klasse):
    """
    Gibt das Klassenobjekt der Klasse aus
    :param klasse:  klasse zu der die Infos benoetigt wird
    :return: Infos zur Klasse
    """
    for k in s.klassen():
        if k.name == klasse:
            return k


def get_room(klasse=None, raumnummer=None):
    """
    Gibt das Raumobjekt zurueck
    :param klasse: klasse von der man den Stammraum haben will
    :param raumnummer: raumnummer des Raums
    :return: Infos zum Raum
    """
    if klasse is None and raumnummer is None:
        for room in s.rooms():
            yield (room)
    elif klasse is not None:
        for room in s.rooms():
            if room.long_name == klasse:
                yield (room)
    elif raumnummer is not None:
        for room in s.rooms():
            if raumnummer in room.name:
                yield (room)


def get_subject():
    """
    Gibt alle Faecher aus
    :return: Infos zum Fach
    """
    for subject in s.subjects():
        yield (subject)


def get_teachers():
    """
    Gibt alle Lehrer aus
    :return: Infos zum Lehrer
    """
    for teacher in s.teachers():
        yield (teacher)


def get_teacher(kuerzel):
    """
    Gibt alle Infos zu einem Bestimmten Lehrer aus
    :param kuerzel: Kuerzel des Lehrers den man sucht
    :return: Infos zum Lehrer
    """
    for teacher in s.teachers():
        if teacher.name == kuerzel:
            return (teacher)


def get_holidays():
    """
    Gibt alle Ferien aus
    :return: Infos zu den Ferien
    """
    for holiday in s.holidays():
        yield (holiday)


def get_departments():
    """
    Gibt alle Abteilungen aus
    :return: Infos zur Abteilung
    """
    for department in s.departments():
        yield (department)


def get_timetable(type, id, start, ende):
    """
    gibt den stundenplan von einer speziellen klasse an einem bestimmten zeitpunkt zurueck
    :param type: welchen stundenplan will man (klasse, teacher, room)
    :param id: ID von wem bzw was man den Stundneplan haben will
    :param start: Ab wann will man den stundenplan haben
    :param ende: Bis wann will man den stundenplan habne
    :return:
    """

    if type == "teacher":
        tt = s.timetable(teacher=id, start=start, end=ende)
    elif type == "klasse":
        tt = s.timetable(klasse=id, start=start, end=ende)
    elif type == "room":
        tt = s.timetable(room=id, start=start, end=ende)
    else:
        raise NameError("unknown type")
    return (tt.to_table())


def get_schulstunde(type, id, tag):
    """
    gibt die einzelnen schulstunden von einer speziellen Klassen, Lehrer oder raeumen an einem bestimmten Tag zurueck

    :param type: welchen stundenplan will man (klasse, teacher, room)
    :param id: ID von wem bzw was man den Stundneplan haben will
    :param tag: Von welchem Tag man den Stundenpan haben will
    :return:
    """
    for stunde in get_timetable(type, id, tag, tag):
        yield stunde


def get_info_from_schulstunde(stunde):
    """
    Gibt die einzelnen Infos zu einer bestimmten Std aus
    :param stunde: Stunde zu der die Infos benoetigt werden
    :return: Infos zu der stunde
    """

    # stunde ist ein Array mit Anfangszeit der Std und allen anderen Infos
    for info in stunde[1]:
        # info ist ein Array mit datum und allen anderen Infos
        for i in info[1]:
            yield i


def print_info(item):
    """
    Printed die Infos welche aus dem Item
    :param item:
    :return:
    """
    for c in item.klassen:
        print(c.name)
    for raum in item.rooms:
        print(str(raum.name) + " - " + raum.long_name)
    for fach in item.subjects:
        print(str(fach.name) + " - " + fach.long_name)
    for lehrer in item.teachers:
        print(str(lehrer.name) + " - " +
              lehrer.fore_name + " - " + lehrer.long_name)

    print(str(item.start) + " - " +
          str(item.end) + " - " +
          str(item.code) + " - " +
          str(item.type))


def get_info(item):
    """
    Gibt die einzelen Infos als array aus
    :param item: enthaelt alle Infos zu der jeweiligen Std
    :return: Array mit allen Infos zur Std
    """
    info = []
    klasse = []
    for c in item.klassen:
        klasse.append(c.name)
    info.append(klasse)
    raum = []
    for r in item.rooms:
        raum.append(r.name)
    info.append(raum)
    fach = []
    for f in item.subjects:
        fach.append(f.name)
    info.append(fach)
    lehrer = []
    for l in item.teachers:
        lehrer.append(l.name)
    info.append(lehrer)

    info.append(str(item.start))
    info.append(str(item.end))

    info.append(item.code)
    return info


def get_substitutions(start, end):
    """
    Gibt alle Substitutions von einem bestimmten Zeitraum aus
    :param start: Anfangs zeitpunkt
    :param end: End zeitpunkt
    :return: Infos zur Substitution
    """
    for sub in s.substitutions(start=start, end=end):
        yield sub


def print_substitutions_info(sub):
    """
    Printed alle Infos zur Substitution
    :param sub: Substitution von der man mehr Infos benoetigt
    :return:
    """
    print(sub.start)
    print(sub.end)
    for k in sub.klassen:
        print(k.name + " - " + str(k.id) + " - " + k.long_name)
    for t in sub.teachers:
        print(t.name + " - " + str(t.id) + " - " + t.fore_name + " - " + t.long_name + " - " + t.surname)
    for f in sub.subjects:
        print(f.name + " - " + str(f.id) + "- " + f.long_name)
    for r in sub.rooms:
        print(r.name + " - " + str(r.id) + " - " + r.long_name)
        print(sub.code)
        print(sub.original_teachers)
    for t in sub.original_teachers:
        print(t.name + " - " + str(t.id) + " - " + t.fore_name + " - " + t.long_name + " - " + t.surname)
    print(sub.type)


def last_weekday(d, weekday):
    """
    Gibt das Datum des Wochentag den man sucht zurueck
    :param d: Tag
    :param weekday:  Wochentag den man sucht
    :return: Datum des Wochentags den man sucht
    """
    days_ahead = weekday - d.weekday()
    if days_ahead >= 0:  # Target day already happened this week
        days_ahead -= 7
    return d + datetime.timedelta(days_ahead)


def get_weekdays_date(day=None):
    """
    Gibt alle Tage der Woche aus
    :param day: Tag von dem man alle Wochentage braucht
    :return:
    """
    if day is None:
        day = datetime.date(2017, 1, 9).today()

        if day.weekday() != 0:
            day = last_weekday(day, 0)
    for t in range(day.weekday(), 6):
        tag = day + datetime.timedelta(t)
        yield (tag)


def get_starttime():
    """
    Gibt ein Array mit den Uhrzeiten wann die einzelnen Schulstunden beginnen aus
    :return: Array mit Beginnzeiten der Schulstunden
    """

    tg = s.timegridUnits()
    start = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for d in tg:
        for tu in d.timeUnits:
            start[int(tu.name)] = str(tu.start)
    return start


def get_endtime():
    """
        Gibt ein Array mit den Uhrzeiten wann die einzelnen Schulstunden enden aus
        :return: Array mit Endzeiten der Schulstunden
    """
    tg = s.timegridUnits()
    end = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for d in tg:
        for tu in d.timeUnits:
            end[int(tu.name)] = str(tu.end)
    return end


def get_stundenplan_array(type, id, d=None):
    """
    Gibt ein Array aus mit den Stundenplan aus
    :param type: Type des Stundenplan (klasse,room, teacher)
    :param id: ID des Objekts von dem man den Stundenplan benoetigt
    :param d: Tag
    :return: Array mit dem Stundenplan
    """
    timetable = [[], [], [], [], [], [], [], [], [], [], [], []], \
                [[], [], [], [], [], [], [], [], [], [], [], []], \
                [[], [], [], [], [], [], [], [], [], [], [], []], \
                [[], [], [], [], [], [], [], [], [], [], [], []], \
                [[], [], [], [], [], [], [], [], [], [], [], []], \
                [[], [], [], [], [], []]

    start = get_starttime()
    for tag in get_weekdays_date(d):
        for stunde in get_schulstunde(type, id, tag):
            for item in get_info_from_schulstunde(stunde):
                if str(item.code) != "cancelled":
                    info = get_info(item)
                    try:
                        timetable[tag.weekday()][start.index(str(item.start)[11:])] = timetable[tag.weekday()][start.index(str(item.start)[11:])] + info
                    except(ValueError):
                        pass


    return timetable


def get_teacher_id(kuerzel):
    """
    Gibt die ID des Lehrers aus
    :param kuerzel: Kurzel des Lehrers von dem man die ID benoetigt
    :return: ID des Lehrers
    """
    for t in get_teachers():
        if t.name == kuerzel:
            return t.id


def get_class_id(name):
    """
    Gibt die ID der Klasse aus
    :param name: Name der Klasse von der die Id benoetigt wird
    :return: iD der Klasse
    """
    for k in get_class(9):
        if k.name == name:
            return k.id


def get_room_id(name):
    """
    Gibt die ID eines Raumes zuruek
    :param name: Name des Raums von dem die ID benoetigt wird
    :return: ID des Raums
    """
    for r in get_room():
        if name in r.long_name or name in r.name:
            return r.id


def write_timetable_to_file(type, id, d=None):
    file = open('timetable.txt', 'w+')
    timetable = get_stundenplan_array(type, id, d)
    for day in timetable:
        for std in day:
            for info in std:
                file.write(str(info))
                file.write(",")
            # print(str(std))

            file.write(';')
        file.write("\n")
    file.close()


#if __name__ == "__main__":
#write_timetable_to_file("room", get_room_id("261"))
