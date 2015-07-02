#!/usr/bin/python2.6
import Skype4Py

skype = Skype4Py.Skype()
skype.Attach()
skype.SendMessage('noviazhang01','hello there')
print 'done send message'
