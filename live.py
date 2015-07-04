import imaplib
import email

class Live():
	def __init__(self):
		import imaplib
		
	def login(self):
	    while True:
			self.imap = imaplib.IMAP4_SSL('imap-mail.outlook.com')
			r, d = self.imap.login('rollyawangga@outlook.com', 'Mambono5')
			assert r == 'OK', 'login failed'
			try:
				print "Connected as ",d
			except self.imap.abort, e:
				print "not connected"
				continue
			#self.imap.logout()
			break
			
	def list(self):
		#self.login()
		return self.imap.list()
	
	def select(self,str):
		return self.imap.select(str)
		
	def inbox(self):
		return self.imap.select("Inbox")
	
	def logout(self):
		return self.imap.logout()
		
	def unread(self):
		r, d = self.imap.search(None, "UNSEEN")
		list = d[0].split(' ')
		latest_id = list[-1]
		r, d = self.imap.fetch(latest_id, "(RFC822)")
		self.raw_email = d[0][1]
		self.email_message = email.message_from_string(self.raw_email)
		return self.email_message
	
	def mailbody(self):
		if self.email_message.is_multipart():
			for payload in self.email_message.get_payload():
				# if payload.is_multipart(): ...
				body = payload.get_payload().split(self.email_message['from'])[0].split('\r\n\r\n2015')[0]
				return body
		else:
			body = self.email_message.get_payload().split(self.email_message['from'])[0].split('\r\n\r\n2015')[0]
			return body

	def mailsubject(self):
		return self.email_message['Subject']		
		
	def mailfrom(self):
		return self.email_message['from']
		
	def mailto(self):
		return self.email_message['to']
		