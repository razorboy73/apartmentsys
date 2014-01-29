#!/usr/bin/env python

"""Send the contents of a directory as a MIME message."""
from local_settings import mailServer, mailPort
import smtplib
# For guessing MIME type based on file name extension
import mimetypes
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


COMMASPACE = ', '

def mailReports(fileBase):
    path = fileBase
    # Create the enclosing (outer) message
    me = "josh@rallyyourgoals.com"
    you = "joshadamkerbel@gmail.com"
    outer = MIMEMultipart()
    outer['Subject'] = 'Contents of directory {}'.format(path)
    outer['To'] = you
    outer['From'] = me
    outer.preamble = 'You will not see this in a MIME-aware mail reader.\n'
    ctype, encoding = mimetypes.guess_type(path)
    if ctype is None or encoding is not None:
            # No guess could be made, or the file is encoded (compressed), so
            # use a generic bag-of-bits type.
            ctype = 'application/octet-stream'
    maintype, subtype = ctype.split('/', 1)
    if maintype == 'text':
        fp = open(path)
        # Note: we should handle calculating the charset
        msg = MIMEText(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'image':
        fp = open(path, 'rb')
        msg = MIMEImage(fp.read(), _subtype=subtype)
        fp.close()
    elif maintype == 'audio':
        fp = open(path, 'rb')
        msg = MIMEAudio(fp.read(), _subtype=subtype)
        fp.close()
    else:
        fp = open(path, 'rb')
        msg = MIMEBase(maintype, subtype)
        msg.set_payload(fp.read())
        fp.close()
        # Encode the payload using Base64
        encoders.encode_base64(msg)
        # Set the filename parameter
    msg.add_header('Content-Disposition', 'attachment', filename=path)
    outer.attach(msg)
    # Now send or store the message
    composed = outer.as_string()
    s = smtplib.SMTP( mailServer,mailPort)
    s.sendmail(me, you, composed)
    print "I hit that email server"
    s.quit()
