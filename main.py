#!/usr/bin/python2.6
import Skype4Py
from gmail import Gmail
import time

skype = Skype4Py.Skype()
skype.Attach()

while True:
	g = Gmail()
	#change to your gmail account and password
	g.login('skype@passionit.net','rollyganteng')
	unread = g.inbox().mail(unread=True)
	try:
		unread[0].fetch()
		subject = unread[0].subject
		message = unread[0].body.split('#')[0]
		print subject
		print message
		skype.SendMessage(message,'Tell me more about your interest in '+subject)
		unread[0].read()
		print 'done send message'
		time.sleep(10)
	except IndexError:
		print "no unread email"
		time.sleep(10)

