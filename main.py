#!/usr/bin/python2.6
import Skype4Py
from gmail import Gmail
import time

skype = Skype4Py.Skype()
skype.Attach()

while True:
	g = Gmail()
	#change to your gmail account and password
	g.login('yourgmail@gmail.com','yourpassword')
	unread = g.inbox().mail(unread=True)
	try:
		unread[0].fetch()
		nomor = unread[0].subject
		pesan = unread[0].body.split('#')[0]
		print nomor
		print pesan
		skype.SendMessage(pesan,'Thank for your contacting me')
		unread[0].read()
		print 'done send message'
		time.sleep(10)
	except IndexError:
		print "no unread email"
		time.sleep(10)

