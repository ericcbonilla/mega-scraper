# Created by Immanuel Amirtharaj

import smtplib


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('megascraper2017@gmail.com', 'goonsquad')
smtpObj.sendmail('megascraper2017@gmail.com', 'ericcbonilla@gmail.com', 'Subject: IT WORKS BROTHER')
