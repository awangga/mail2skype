#!/usr/bin/python2.6
import Skype4Py

print 'please allow Skype4Py to connect to your skype appication client'
skype = Skype4Py.Skype()
skype.Attach()
print 'done if no error'
