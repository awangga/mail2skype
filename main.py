#!/usr/bin/python2.6
import Skype4Py
from gmail import Gmail
import time
import config
import parser

skype = Skype4Py.Skype()
skype.Attach()

while True:
	g = Gmail()
	g.login(config.email,config.password)
	unread = g.inbox().mail(unread=True)
	try:
		unread[0].fetch()
		subject = unread[0].subject
		message = unread[0].body
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

