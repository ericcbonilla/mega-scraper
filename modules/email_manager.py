# Created by Immanuel Amirtharaj
# Friday, August 11, 2017

import smtplib

class EmailObject:
	def __init__(self, destination, subject, description):
		self.destination = destination
		self.subject = subject
		self.description = description
		

def send_message(destination, subject, description):
	emailObject = EmailObject(destination, subject, description)
	smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
	smtpObj.ehlo()
	smtpObj.starttls()
	smtpObj.login('megascraper2017@gmail.com', 'goonsquad')

	payload = 'Subject:' + emailObject.subject
	payload = payload + '\n'
	payload = payload + emailObject.description

	smtpObj.sendmail('megascraper2017@gmail.com', emailObject.destination, payload)


def email_tests():
	send_message('megascraper2017@gmail.com', 'Email Test', 'This is an email test')




if __name__ == '__main__':
	email_tests()