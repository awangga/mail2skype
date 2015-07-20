#!/usr/bin/python2.6
def getSkype(str):
	stack = []
	arrstr = getSplit(str)
	arrstr = get6to32char(arrstr)
	if len(arrstr) == 1:
		stack.append(arrstr[0])
	else:
		for istr in arrstr:
			if hasNumbers(istr):
				stack.append(istr)
			elif hasDot(istr):
				stack.append(istr)
			elif hasDash(istr):
				stack.append(istr)
			elif hasUnderscore(istr):
				stack.append(istr)
			elif hasComma(istr):
				stack.append(istr)
	if stack == []:
		for istri in arrstr:
			if not hasSpecialChar(istri):
				stack.append(istri)
	if stack == []:
		stack = arrstr
	return stack

def haveWord(wrd,msg):
	if wrd in msg.lower():
		return True
	else:
		return False

def sendChats(skypeidarr,intro,subj,msg):
	i = 0
	while i < len(skypeidarr):
		skype.SendMessage(skypeidarr[i],intro+subj+"\r\n with Content : \r\n"+msg)
		i += 1

def get6to32char(arrstr):
    stack = []
    i = 0
    while i < len(arrstr):
    	if (len(arrstr[i]) >= 6 and len(arrstr[i]) <= 32):
    		stack.append(arrstr[i])
    	i += 1
    return stack

def getSplit(str):
	return str.split('-- ')[0].split('\r\nOn ')[0].replace('\r\n',' ').split(' ')

def hasDot(str):
	if hasSpecialChar(str):
		return False
	elif '.' in str:
		return True

def hasComma(str):
	if hasSpecialChar(str):
		return False
	elif ',' in str:
		return True

def hasDash(str):
	if hasSpecialChar(str):
		return False
	elif '-' in str:
		return True
    
def hasUnderscore(str):
	if hasSpecialChar(str):
		return False
	elif '_' in str:
		return True

def hasNumbers(str):
	return any(char.isdigit() for char in str)

def hasSpecialChar(str):
	if '/' in str:
		has = True
	elif '=' in str:
		has = True
	elif '@' in str:
		has = True
	elif '+' in str:
		has = True
	elif '(' in str:
		has = True
	elif '[' in str:
		has = True
	elif '&' in str:
		has = True
	elif '#' in str:
		has = True
	elif '$' in str:
		has = True
	elif '^' in str:
		has = True
	elif ':' in str:
		has = True
	elif ';' in str:
		has = True
	elif '<' in str:
		has = True
	elif '?' in str:
		has = True
	elif '{' in str:
		has = True
	elif '%' in str:
		has = True
	elif '*' in str:
		has = True
	elif '~' in str:
		has = True
	elif '|' in str:
		has = True
	elif ')' in str:
		has = True
	elif '}' in str:
		has = True
	elif ']' in str:
		has = True
	elif '>' in str:
		has = True
	elif '--' in str:
		has = True
	elif '__' in str:
		has = True
	elif str[-1] == '.':
		has = True
	elif str[-1] == ',':
		has = True
	else:
		has = False
	return has

# this is just a variable
tangerine = "Living reflection of a dream"