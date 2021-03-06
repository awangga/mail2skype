#!/usr/bin/python2.6
import Skype4Py
import outlook
import time
import config
import parser

skype = Skype4Py.Skype()
skype.Attach()

def checkingFolder(folder):
	mail = outlook.Outlook()
	mail.login(config.outlook_email,config.outlook_password)
	mail.readOnly(folder)
	print "  Looking Up "+folder
	try:
		unread_ids_today = mail.unreadIdsToday()
		print "   unread email ids today : "
		print unread_ids_today
		unread_ids_with_word = mail.getIdswithWord(unread_ids_today,'skype id')
		print "   unread email ids with word Skype ID today : "
		print unread_ids_with_word
	except:
		print config.nomail
	#fetch Inbox folder
	time.sleep(3)
	mail = outlook.Outlook()
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
			if mail.mailreplyto():
				sendto =  mail.mailreplyto()
			else:
				sendto = mail.mailfrom().split('>')[0].split('<')[1]
			print "  sending reply message..."
			print "  to :"+sendto
			print "  subject : "+subject
			print "  content : "+config.replymessage
			mail.sendEmail(sendto,"Re : "+subject,config.replymessage)
			time.sleep(3)
	except:
		print config.noword
		time.sleep(3)


while True:
	try:
		#checking ids in Inbox Folder
		print config.checkinbox
		checkingFolder('Inbox')
		#checking Junk Folder
		print config.checkjunk
		checkingFolder('Junk')
	except:
		print "Retrying..."
		continue
