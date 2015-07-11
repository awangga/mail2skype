#!/usr/bin/python2.6
import Skype4Py
import live
import time
import config
import parser

skype = Skype4Py.Skype()
skype.Attach()

def checkingFolder(folder):
	mail = live.Live()
	mail.login(config.outlook_email,config.outlook_password)
	mail.readOnly(folder)
	try:
		unread_ids_today = mail.unreadIdsToday()
		unread_ids_with_word = getIdswithWord(unread_ids_today,'skype id')
	except:
		print config.nomail
	#fetch Inbox folder
	mail = live.Live()
	mail.login(config.outlook_email,config.outlook_password)
	mail.select(folder)
	try:
		for id_w_word in unread_ids_with_word:
			mail.getEmail(id_w_word)
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
		print config.noword
		time.sleep(10)


while True:
	#checking ids in Inbox Folder
	print config.checkinbox
	checkingFolder('Inbox')
	#checking Junk Folder
	print config.checkjunk
	checkingFolder('Junk')
