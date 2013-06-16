#!/usr/bin/env python
# coding=utf-8
import os
import json
import urllib
import hashlib

import lxml.etree
import redis
import tornado.web
from random import choice
from config import KT
from helper import HelperHandler

smdmy = ''' 你的关键词，我们的机器人会在一个工作日内更新。并且自动回复你  '''
wxTpl = '''<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[%s]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>'''
WeixinToken = '654321'


class Talk():
    def talk(self,value):
        kv = redis.StrictRedis()
        contact_list = []
        search = KT['c'] + "*"+ value.encode("UTF-8") + "*"
        search_list_all = kv.keys(search)#如果没有，返回[]
        if search_list_all:
            for t in search_list_all:
                c = kv.get(t)
                c = json.loads(c)
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
        kv = redis.StrictRedis()
        if body:
                dom = lxml.etree.fromstring(body)
                ToUserName = dom.find('ToUserName').text
                FromUserName = dom.find('FromUserName').text
                CreateTime = dom.find('CreateTime').text
                MsgType = dom.find('MsgType').text
                Content = dom.find('Content').text
                
                T = Talk()
                T_contact_list = T.talk(Content)
                T_contact_list = json.loads(T_contact_list)
                contact_list = T_contact_list
                #contact_list = []
                
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
    (r"/1984", WXInterface),
]
