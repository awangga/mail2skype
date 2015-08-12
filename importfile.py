#!/usr/bin/python2.6
import Skype4Py
import time
import config
import csv
import parser


skype = Skype4Py.Skype()
skype.Attach()

with open(config.filename, 'rb') as f:
	reader = csv.reader(f, delimiter=config.delimiter, skipinitialspace=True, quoting=csv.QUOTE_MINIMAL, quotechar=b'"', lineterminator="\n")
	i = 0
	for row in reader:
		#skype.SendMessage(skypeidarr[i],config.intromsg+subject+"\r\n with Content : \r\n"+message)
		skype_id = row[config.skypecolumn]
		a = parser.filterSkype(skype_id)
		if a:
			print "send message to : "+a[0]
			skype.SendMessage(a[0],config.intro)
			a += 1
