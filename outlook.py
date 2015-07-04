#!/usr/bin/python2.6
import Skype4Py
import live
import time
import config
import parser

skype = Skype4Py.Skype()
skype.Attach()

while True:
	mail = live.Live()
	mail.login()
	mail.inbox()
	try:
		mail.unread()
		subject = mail.mailsubject()
		message = mail.mailbody()
		skypeidarr = parser.skypeid(message)
		print subject
		print skypeidarr
		i = 0
		while i < len(skypeidarr):
			skype.SendMessage(skypeidarr[i],config.intromsg+subject)
			i += 1
		unread[0].read()
		config.success()
		time.sleep(10)
	except IndexError:
		print config.nomail
		time.sleep(10)

