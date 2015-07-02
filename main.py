#!/usr/bin/python2.6
import Skype4Py
from gmail import Gmail

skype = Skype4Py.Skype()
skype.Attach()

g = Gmail()
g.login('sms@kitaklik.com','rollygantengsekali')
unread = g.inbox().mail(unread=True, sender="awg@kitaklik.com")
try:
	unread[0].fetch()
	nomor = unread[0].subject.split('+')[1]
	pesan = unread[0].body.split('#')[0]
	print nomor
	print pesan
	skype.SendMessage(pesan,'Thank for your contacting me')
	unread[0].read()
	print 'done send message'
except IndexError:
	print "no unread email"

