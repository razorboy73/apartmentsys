# Import smtplib for the actual sending function
#not being used - just for historical purposes only
from local_settings import mailServer, mailPort
import smtplib
from email.mime.text import MIMEText
import os
import fnmatch
import smtplib
import string
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.Utils import formatdate

def emailSending(fileToSend):
    # Import the email modules we'll need
    # Open a plain text file for reading.  For this example, assume that
    # the text file contains only ASCII characters.
    fp = open(fileToSend, 'rb')
    # Create a text/plain message
    msg = MIMEText(fp.read())
    fp.close()

    me = "josh@rallyyourgoals.com"
    you = "joshadamkerbel@gmail.com"
    msg['Subject'] = 'The contents of {}'.format(fileToSend)
    msg['From'] = "josh@rallyyourgoals.com"
    msg['To'] = "joshadamkerbel@gmail.com"
    #path = "/Users/workhorse/thinkful/apartments/2014-01-27faoYzvtfWtgsbzWU/January2014/January2014buildings.txt"
    # Send the message via our own SMTP server, but don't include the
    # envelope header.
    #s = smtplib.SMTP('localhost')
    s = smtplib.SMTP( mailServer,mailPort)
    s.sendmail(me, [you], msg.as_string())
    s.quit()

