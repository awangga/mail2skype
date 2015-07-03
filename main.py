#!/usr/bin/python2.6
import Skype4Py
from gmail import Gmail
import time
import config

skype = Skype4Py.Skype()
skype.Attach()

while True:
	g = Gmail()
	g.login(config.email,config.password)
	unread = g.inbox().mail(unread=True)
	try:
		unread[0].fetch()
		subject = unread[0].subject
		message = unread[0].body.split('#')[0]
		print subject
		print message
		skype.SendMessage(message,config.intromsg+subject)
		unread[0].read()
		config.success()
		time.sleep(10)
	except IndexError:
		print "no unread email"
		time.sleep(10)

