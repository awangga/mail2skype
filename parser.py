#!/usr/bin/python2.6
def skypeid(str):
    stack = []
    i = 0
    str = str.replace('\r\n',' ').split(' ')
    while i < len(str):
    	if len(str[i]) >= 6:
    		stack.append(str[i])
    	i += 1
    return stack

# this is just a variable
tangerine = "Living reflection of a dream"