#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pymongo import MongoClient
import itchat
from itchat.content import *
import re

def deal_word(keywords):
        keywords = re.sub(r'á|Á','a',keywords)
        keywords = re.sub(r'é|É','e',keywords)
        keywords = re.sub(r'í|Í','i',keywords)
        keywords = re.sub(r'ó|Ó','o',keywords)
        keywords = re.sub(r'ú|Ú','u',keywords)
        keywords = keywords.lower()
        return keywords

#@itchat.msg_register(TEXT, isGroupChat=True)
@itchat.msg_register(TEXT)
def text_reply(msg):
    #if msg.isAt:
        #msg.user.send(u'@%s\u2005I received: %s' % (
            #msg.actualNickName, msg.text))
    text = msg.text
    #print(text)
    text = re.search(r'(?<=\@灯\s).*',text,re.I)
    if text!=None:
    #print(text.group())
        text = text.group()
        if re.match(r'[a-zA-ZáéíóúÁÉÍÓÚ]+$',text):
            text = deal_word(text)
            client = MongoClient('localhost:27017')
            db = client.beltadb
            try:
                dic_a = db.Belta_word.find({"Belta_nic":text},{"English":1,"_id":0})[0]
                res = dic_a['English']
                msg.user.send(res)
            except:
                try:
                    dic_b = db.Belta_word.find({"English":re.compile(text)},{"Belta_word":1,"Belta_nic":1,"_id":0})[0]
                    msg.user.send(dic_b["Belta_word"])
                except:
                    msg.user.send(u'no result!' )
        else:
            msg.user.send(u'%s is not a valid term!' %(text))

itchat.auto_login(True)
itchat.run(True)