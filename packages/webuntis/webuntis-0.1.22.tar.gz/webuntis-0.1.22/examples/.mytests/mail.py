import smtplib
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# from http://stackoverflow.com/questions/10147455/trying-to-send-email-gmail-as-mail-provider-using-python
import datetime
import pytz

try:
    with open("/etc/timezone") as f:
        MY_TIMEZONE = f.read().strip()
except IOError:
    MY_TIMEZONE = 'Europe/Vienna'

class Mail(object):
    def __init__(self, email, password, server):
        """

        :type password: basestring
        :type email: basestring
        """
        self.email = email
        self.password = password
        self.server = server
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, toemail, subject, body, copy2self = False):
        """
        :param toemail:
        :type toemail: basestring
        :param subject:
        :type subject: basestring
        :param body:
        :type body: basestring
        :param copy2self: send bcc to sender
        :type copy2self: boolean
        """
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + self.email,
            "MIME-Version: 1.0",
            "Content-Type: text/plain"]
        if copy2self:
            headers += [ "cc: " + self.email]
            toemail = [toemail, self.email]
        headers = "\r\n".join(headers)
        self.session.sendmail(
            self.email,
            toemail,
            headers + "\r\n\r\n" + body)

    def send_message_ical(self, toemail, subject, body, ical, copy2self = False):
        """
        send mail to TOMAIL

        :param toemail:
        :type toemail: basestring
        :param subject:
        :type subject: basestring
        :param body:
        :type body: basestring
        :param ical:
        :type ical: basestring
        :param copy2self: send bcc to sender
        :type copy2self: boolean
        """
        msg = MIMEMultipart()
        subject = Header(subject, "utf-8")
        msg['Subject'] = subject
        msg['From'] = self.email
        msg['To'] = toemail
        msg.preamble = body
        if copy2self:
            msg[ "cc"] = self.email
            toemail = [ toemail, self.email]
        part_email = MIMEText(body)
        msg.attach(part_email)

        if ical:
            part_cal = MIMEText(ical, 'calendar;method=REQUEST')
            # msgAlternative.attach(part_cal)
            msg.attach(part_cal)

            ical_atch = MIMEBase('application/ics', ' ;name="%s"' % "invite.ics")
            ical_atch.set_payload(ical)
            encoders.encode_base64(ical_atch)
            ical_atch.add_header('Content-Disposition', 'attachment; filename="%s"' % "invite.ics")
            msg.attach(ical_atch)

        self.session.sendmail(self.email, toemail, msg.as_string())


def to_utc(d):
    """
    tarnslate untis-time (without timezone) to UTC-timezone

    :param d: untis time
    :type d: datetime.datetime
    :return: time as UTC
    :rtype:  datetime.datetime
    """
    tz = pytz.timezone(MY_TIMEZONE)
    return tz.normalize(tz.localize(d)).astimezone(pytz.utc)


def createical(txt, sdatetime, etime, location, email):
    """

    :param txt:
    :type txt: basestring
    :param sdatetime:
    :type sdatetime: datetime.datetime
    :param etime:
    :type etime: datetime.time
    :param location:
    :type location: basestring
    :param email:
    :type email: basestring
    :return:
    :rtype: basestring
    """
    if not sdatetime:
        return None
    date_format = "%Y%m%dT%H%M%SZ"
    sdatetime = to_utc(sdatetime)
    etime = to_utc(etime)
    tz = pytz.timezone(MY_TIMEZONE)
    now = datetime.datetime.now(tz).strftime(date_format)

    starttime = sdatetime.strftime(date_format)
    endtime = etime.strftime(date_format)
    rand = starttime
    # ?? PARTSTAT=ACCEPTED
    ical = """
BEGIN:VCALENDAR
PRODID:Webuntis Parser V2
VERSION:0.1
CALSCALE:GREGORIAN
METHOD:REQUEST
BEGIN:VEVENT
DTSTART:{starttime}
DTEND:{endtime}
DTSTAMP:{now}
ORGANIZER:HTL
UID: {rand}@webuntis
ATTENDEE;CUTYPE=INDIVIDUAL;ROLE=REQ-PARTICIPANT;PARTSTAT=ACCEPTED;RSVP=FALSE;CN={email};X-NUM-GUESTS=0:mailto:{email}
CREATED: {now}
DESCRIPTION:{txt}
LAST-MODIFIED:{now}
LOCATION:{location}
SEQUENCE: 1
STATUS:CONFIRMED
SUMMARY:{txt}
TRANSP:OPAQUE
BEGIN:VALARM
ACTION:DISPLAY
DESCRIPTION:{txt}
TRIGGER:-P0DT0H15M0S
END:VALARM
END:VEVENT
END:VCALENDAR
""".format(**locals())
    return ical

