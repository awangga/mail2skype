#!/usr/bin/python2.6
import Skype4Py
import live
import time
import config
import parser

skype = Skype4Py.Skype()
skype.Attach()

while True:
	print config.checkinbox
	mail = live.Live()
	mail.login(config.outlook_email,config.outlook_password)
	mail.inbox()
	try:
		mail.unread()
		subject = mail.mailsubject()
		message = mail.mailbody()
		skypeidarr = parser.getSkype(message)
		print subject
		print skypeidarr
		i = 0
		while i < len(skypeidarr):
			skype.SendMessage(skypeidarr[i],config.intromsg+subject+"\r\n with Content : \r\n"+message)
			i += 1
		config.success()
		print "sending reply message..."
		print "to :"+mail.mailfrom().split('>')[0].split('<')[1]
		print "subject : "+subject
		print "content : "+config.replymessage
		mail.sendEmail(mail.mailfrom().split('>')[0].split('<')[1],"Re : "+subject,config.replymessage)
		time.sleep(10)
	except:
		print config.nomail
		time.sleep(10)
	print config.checkjunk
	mail = live.Live()
	mail.login(config.outlook_email,config.outlook_password)
	mail.junk()
	try:
		mail.unread()
		subject = mail.mailsubject()
		message = mail.mailbody()
		if 'skype' in message.lower():
			skypeidarr = parser.skypeid(message)
			print subject
			print skypeidarr
			i = 0
			while i < len(skypeidarr):
				skype.SendMessage(skypeidarr[i],config.intromsg+subject)
				i += 1
			config.success()
		else:
			print config.noword
		time.sleep(10)
	except:
		print config.nomail
		time.sleep(10)
