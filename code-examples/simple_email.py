# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
textfile = "file.txt"
with open(textfile) as fp:
    # Create a text/plain message
    msg = MIMEText(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = "immanuelda@gmail.com"
msg['To'] = "immanuelda@gmail.com"

# Send the message via our own SMTP server.
s = smtplib.SMTP('localhost', 8025)
s.send_message(msg)
s.quit()