#!/usr/bin/env python
# coding=utf-8
import os
import json
import urllib
import hashlib

import sae.kvdb as redis
import lxml.etree

import tornado.web

from random import choice

from config import KT
from config import WeixinToken
from config import WeixinUrl
from config import smdmy
from helper import HelperHandler

wxTpl = '''<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>'''


class Talk():
    def talk(self,value):
		kv = redis.KVClient()
		contact_list = []
		wx = [i for i in kv.get_by_prefix(KT['c']  + value.encode("UTF-8"))]
		for t in wx:
			c = json.loads(t[1])
			contact_list.append(c)
		return json.dumps(contact_list)


class WXInterface(HelperHandler):
    def get(self):
        signature = self.get_argument("signature","ccdjh")
        timestamp = self.get_argument("timestamp","ccdjh")
        nonce = self.get_argument("nonce","ccdjh")
        echostr = self.get_argument("echostr","ccdjh")
        token = WeixinToken
        
        k = [token,timestamp ,nonce]
        k.sort()
        content = ''.join(k)
        c = hashlib.sha1(content).hexdigest()
        if signature != c:
            self.write('sibai')
        else:
            self.write(echostr)

    def post(self):
        body = self.request.body
        #kv = redis.StrictRedis()
        kv = redis.KVClient()
        if body:
                dom = lxml.etree.fromstring(body)
                ToUserName = dom.find('ToUserName').text
                FromUserName = dom.find('FromUserName').text
                CreateTime = dom.find('CreateTime').text
                MsgType = dom.find('MsgType').text
                Content = dom.find('Content').text
                
                T = Talk()
                T_contact_list = T.talk(Content)
                contact_list = json.loads(T_contact_list)

                
                if contact_list:
                    contact = choice(contact_list)
                    contact = contact['content']
                    contactTalk = wxTpl % (FromUserName, ToUserName,CreateTime,MsgType,contact)
                    self.write(contactTalk)
                else:
                    contact = smdmy
                    contactTalk = wxTpl % (FromUserName, ToUserName,CreateTime,MsgType,contact)
                    self.write(contactTalk)
        else:
                pass
        

goInterface = [
    (WeixinUrl, WXInterface),
]
