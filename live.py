import imaplib
def login():
    while True:
		imap = imaplib.IMAP4_SSL('imap-mail.outlook.com')
		r, d = imap.login('rollyawangga@outlook.com', 'Mambono5')
		assert r == 'OK', 'login failed'
		try:
			print imap.list()
			imap.select('Inbox')
		except imap.abort, e:
			print "not connected"
			continue
		imap.logout()
		break