#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from pymongo import MongoClient
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import os
import time
import pyperclip
import re

m = PyMouse()
k = PyKeyboard()

#x_dim, y_dim = m.screen_size()
#m.click(x_dim/2, y_dim/2, 1)
#time.sleep(1)
keywords_last = ""

while 1:

	m.click(600, 115, 1)
	time.sleep(1)

	#time.sleep(1)
	k.press_keys(['Command','a'])
	time.sleep(1)
	k.press_keys(['Command','c'])
	time.sleep(1)
	#chat_string = "@bot sabaka @bot"
	chat_string = pyperclip.paste().encode('utf-8')
	#pyperclip.copy("")
	#print chat_string
	keyword = re.search(r'(?<=\@bot\s).*(?=\s\@bot)',chat_string,re.I)
	if keyword:
		m.click(493,154,2)
		time.sleep(1)
		m.click(503,164,1)
		time.sleep(1)
		keywords = keyword.group()
		print "keywords is: "+keywords
		if keywords != keywords_last:
			keywords_last = keywords
			print len(keywords)
			if re.match(r'[a-zA-ZáéíóúÁÉÍÓÚ]+$',keywords):
				keywords = re.sub(r'á|Á','a',keywords)
				keywords = re.sub(r'é|É','e',keywords)
				keywords = re.sub(r'í|Í','i',keywords)
				keywords = re.sub(r'ó|Ó','o',keywords)
				keywords = re.sub(r'ú|Ú','u',keywords)

				keywords = keywords.lower()
				#keywords = keywords[0].upper()+keywords[1:]
				client = MongoClient('localhost:27017')
				db = client.beltadb
				try:
					dic_a = db.Belta_word.find({"Belta_nic":keywords},{"English":1,"_id":0})[0]
					res = dic_a['English']
					print type(res)
					res1 = res.encode("utf-8")
					print type(res1)
					pyperclip.copy(res1)
					#a = pyperclip.paste()
					#print a
					#pyperclip.copy(a)
					#time.sleep(2)
					m.click(700,740,1)
					time.sleep(1)
					k.press_keys(['Command','v'])
					time.sleep(1)
					#k.press_key('Return')
					m.click(1140,783,1)
					#os._exit(0)

				except:
					warning = keywords+" is not a valid term"
					pyperclip.copy(warning)
					m.click(700,740,1)
					k.press_keys(['Command','v'])
					time.sleep(1)
					m.click(1140,783,1)
					#time.sleep(1)
					#k.type_string(keywords+" is not a valid term")
					print "find nothing"
					#os._exit(0)
			else:
				if keywords=="911":
					pyperclip.copy("")
					os._exit(0)
				#m.click(700,740)
				#k.type_string("Invalid Input")
				print "invalid input"
	
	pyperclip.copy("")		#os._exit(0)
	time.sleep(5)
