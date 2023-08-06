#! /usr/bin/env python2
# -*- coding: utf-8 -*-

import argparse
import collections
import datetime
import logging
import os
import shelve
import sys

from time import sleep

import mail
import webuntis
import webuntis.objects
from log import my_logger

# from typing import Dict, Any, List

try:
    # noinspection PyUnresolvedReferences
    import secret
except ImportError as ie:
    with open("sample-secret.py", "w") as f:
        f.write("""
# fill out & rename to secret.py
untis_username = "your untis username"
untis_passwd = "topSecret"

mail_sender = "your-email@gmail.com"
mail_passwd = "your-email-password"
mail_server = "smtp.your.provider"

copy_email = mail_sender

teacher_email = "@some.school"
""")
    my_logger.error("Import failed: " + str(ie) + "\nPlease edit `sample-secret.py` and rename to `secret.py`")
    sys.exit(99)

if False:
    import vcr
else:
    from contextlib import contextmanager

    class VCR:
        @contextmanager
        def use_cassette(self, _):
            yield None

    vcr = VCR()

# Default Values
sendmail = False
sendcopy = False
sendcc = False
cachefilename = "webuntis.cache"
ignorecache = False
subject = "[Webuntis Changes V3] "
days = 21
verbose = False


@contextmanager
def webuntis_login():
    """ create a session context

    :returns webuntis.Session
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
    s.logout(suppress_errors=True)
    my_logger.info("Logged out")


def get_subst(session, start_date, end_date, teachers):
    """
    get all substitutions for teachers in the interval start-end

    :rtype: Dict[str, List[webuntis.objects.SubstitutionObject]]
    :param start_date: datetime.datetime
    :param end_date: datetime.datetime
    :param session: webuntis.Session
    :param teachers: dict[string, Substitution_Data]
    """
    substitutions = session.substitutions(start=start_date, end=end_date)

    my_logger.info("Suppl count: " + str(len(substitutions)))
    substitutions = substitutions.combine()

    my_logger.info("Suppl count: " + str(len(substitutions)))
    subst_list = collections.defaultdict(list)  # Dict[str, List[webuntis.objects.SubstitutionObject]]
    for sub in substitutions:
        try:
            names = set(x.name for x in sub.teachers)
            st = names & teachers
            for t in st:
                subst_list[t].append(sub)
        except IndexError:
            pass
    return subst_list


def join(delim, *args):
    """
    join the str() of all args with delimiter delim (ignore emtpy arguments)
    :param delim:
    :type delim: basestring
    :param args:
    :type args: object
    :return:
    :rtype:
    :rtype: basestring
    """
    return delim.join(str(a) for a in args if a)


@contextmanager
def maybe_cache(ignore):
    if ignore:
        my_logger.info("NO cache")
        yield dict()
    else:
        my_logger.info("WITH cache " + cachefilename)
        # TODO: python3 -- with
        s = shelve.open(cachefilename, writeback=True)
        yield s
        s.close()


CODE = {
    "cancel": "cancellation",
    "subst": "teacher substitution",
    "add": "additional period",
    "shift": "shifted period",
    "rmchg": "room change",
    "free": "cancellation",
    None: ""
}

CODE_DE = {
    "cancel": "Entfall",
    "subst": "Supplierung",
    "add": "Zusaetzliche Stunden",
    "shift": "Verschoben",
    "rmchg": "Raumaenderung",
    "free": "Entfall",
    None: ""
}


def handle_request(subjectstart):
    with webuntis_login() as sess, \
            maybe_cache(ignorecache) as suppl_cache:

        cacheline = str(sess.last_import_time().date)
        my_logger.info("lastImportTime: " + cacheline)
        if not ignorecache and cacheline in suppl_cache:
            my_logger.info("NO CHANGE -- same lastImportTime")
            # return
        suppl_cache[cacheline] = True

        yearend = sess.schoolyears().current.end

        start = datetime.date.today()
        if start > yearend.date():
            sys.exit(99)

        end = start + datetime.timedelta(days=days)
        end = min(end, yearend.date())
        my_logger.info(join("REQ", "Date Start", start, "End", end))

        my_subst_list = get_subst(sess, start, end,
                                  wanted_teachers)  # type: Dict[str, List[webuntis.objects.SubstitutionObject]]

        if sendcopy or sendmail:
            gm = mail.Mail(secret.mail_sender, secret.mail_passwd, secret.mail_server)

        for teacher1, suppl in my_subst_list.items():
            for subst in suppl:
                try:
                    st = {t.name for t in subst.teachers}
                    if len(st) > 20:
                        continue
                    for teacher in {teacher1} | (st & wanted_teachers):
                        no_ical = ""
                        mailaddr = teacher + secret.teacher_email
                        my_logger.info("Teacher: " + teacher)
                        my_logger.debug(join(" ", "Suppl:", teacher1, subst.start))
                        r = join(",", *subst.rooms)
                        k = join(",", *subst.klassen)
                        g = join(",", *subst.subjects)
                        c = CODE_DE.get(subst.type, subst.type or " ")
                        if subst.original_teachers:
                            c += " (statt " + join(",", *subst.original_teachers) + ")"
                        if len(st) > 1:
                            c += " (mit " + join(",", *(st - {teacher})) + ")"
                        subject = subjectstart + join(" - ", teacher1, subst.start, subst.end.time(), k, g, r, c)
                        my_logger.info("Subject: " + subject)
                        cacheline = str(teacher) + ":" + str(subst)
                        if ignorecache or (cacheline not in suppl_cache):
                            suppl_cache[cacheline] = True
                            if subst.type != "cancel":
                                if withoutical:
                                    ical = ""
                                else:
                                    ical = mail.createical(subject, subst.start, subst.end, r, mailaddr)
                                my_logger.debug("Ical: " + ical.replace("\n", "\n    "))
                                if sendmail:
                                    gm.send_message_ical(mailaddr, subject, subject, ical, sendcc)
                                    my_logger.info("Mail+ical sent")
                                    sleep(args.pause)
                                else:
                                    my_logger.debug("NO Mail+ical sent")
                                if sendcopy:
                                    gm.send_message_ical(secret.copy_email, subjectcopy, teacher + "\n" + subject, ical,
                                                         sendcc)
                                    my_logger.info("Mail+ical sent (copy)")
                                    sleep(args.pause)
                                else:
                                    my_logger.debug("NO Mail+ical sent (copy)")
                            else:
                                no_ical += subject + "\n"
                        else:
                            my_logger.debug("Already in cache: " + cacheline)
                        if no_ical:
                            my_logger.info("Teacher Mail:" + teacher + "\n    " + no_ical.replace("\n", "\n    "))
                            if sendmail:
                                gm.send_message(mailaddr, subject, teacher + "\n" + no_ical)
                                my_logger.info("Mail sent")
                                sleep(args.pause)
                            else:
                                my_logger.debug("NO Mail sent")
                            if sendcopy:
                                gm.send_message(secret.copy_email, subjectcopy, teacher + "\n" + no_ical)
                                my_logger.info("Mail sent (copy)")
                                sleep(args.pause)
                            else:
                                my_logger.debug("NO Mail sent (copy)")
                except Exception as e:
                    my_logger.error("=*=" * 20)
                    my_logger.error("Exception:" + str(e), stack_info=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Check Webuntis for "Supplierungen".')
    parser.add_argument('-m', '--sendmail', action='store_true', help='send mail to user', dest="sendmail",
                        default=sendmail)
    parser.add_argument('-c', '--sendcopy', action='store_true', help='send copy of mail', dest="sendcopy",
                        default=sendcopy)
    parser.add_argument('-b', '--sendcc', action='store_true', help='send bcc to sender', dest="sendcc",
                        default=sendcc)
    parser.add_argument('-s', '--subject', help='subject of mail', dest="subject", default=subject)
    parser.add_argument('-f', '--cachefile', help='cache file', dest="cachefilename", default=cachefilename)
    parser.add_argument('-i', '--ignorecache', action='store_true', help='ignore cache file', dest="ignorecache",
                        default=ignorecache)
    parser.add_argument('-d', '--days', type=int, help='number of days to lock ahead', default=days)
    parser.add_argument('-w', '--withoutical', action='store_true', help='no ical attachment')
    parser.add_argument('teachers', metavar='teachers', type=str, nargs='+',
                        help='the teachers to look for')
    parser.add_argument("-v", "--verbose", action='store_true', help='show more info', dest="verbose", default=verbose)
    parser.add_argument("-p", "--pause", type=float, help='seconds to sleep after each mail', default=3)
    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

    sendmail = args.sendmail
    sendcopy = args.sendcopy
    sendcc = args.sendcc
    subject = args.subject
    subjectcopy = subject + " - Kopie"
    cachefilename = args.cachefilename
    ignorecache = args.ignorecache
    days = args.days
    withoutical = args.withoutical
    wanted_teachers = set(args.teachers)

    my_logger.info("Webuntis starting -------------------------------------------------------------------------------")
    my_logger.info(join(" ", "ARGS", str(args)))
    my_logger.info(join(" ", "SENDMAIL", str(sendmail), "SENDCOPY", str(sendcopy), "IGNORECACHE", str(ignorecache)))
    my_logger.info(join(" ", "CACHEFILENAME", cachefilename, "exists", str(os.path.exists(cachefilename))))
    my_logger.info("teachers:" + str(wanted_teachers))

    try:
        webuntis.utils.remote._request_getid = lambda: "4711"
        with vcr.use_cassette("test.yml"):
            handle_request(subject)
    except Exception as e:
        my_logger.error("=*=" * 20)
        my_logger.error("Exception:" + str(e))
        raise
