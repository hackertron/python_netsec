#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText

# (extended hello) ehlo test.com
#  mail from:  test@ftest.com
#  rcpt to:  me@me.com
#  data

s = smtplib.SMTP("", 25)
#s.login("user", "password")

try:
#  could use the following for a MIME message
#    f = open("myfile", "r")
#    m = MIMEText(f.read())
#    f.close()
#    m['To'] = ""
#    m['From'] = ""
#    m['Subject'] = "This is a message"

    m = "\nThis is a message from the last session"
    s.sendmail("", "", m)
    #  send the MIME message
    # s.send_message(m)
    print("Finished sending message")
except Exception as e:
    print("Unable to send message: ", e)

s.quit()
