# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText
fileToSend = "buildings.txt"
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

# Send the message via our own SMTP server, but don't include the
# envelope header.
#s = smtplib.SMTP('localhost')
s = smtplib.SMTP( "mail.*****",**** )
s.sendmail(me, [you], msg.as_string())
s.quit()