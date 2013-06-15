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
from talk import Talk
from talk import JiebaTalk

wxTpl = '''

<xml>
 <ToUserName><![CDATA[%s]]></ToUserName>
 <FromUserName><![CDATA[%s]]></FromUserName>
 <CreateTime>%s</CreateTime>
 <MsgType><![CDATA[%s]]></MsgType>
 <Content><![CDATA[%s]]></Content>
 <FuncFlag>0</FuncFlag>
 </xml>

'''
SinaWeixinToken = '876'

smdmy = ''' 你的关键词，我们的机器人会在一个工作日内更新。并且自动回复你  '''


class WXInterface(HelperHandler):
    def get(self):
        signature = self.get_argument("signature","ccdjh")
        timestamp = self.get_argument("timestamp","ccdjh")
        nonce = self.get_argument("nonce","ccdjh")
        echostr = self.get_argument("echostr","ccdjh")
        token = SinaWeixinToken
        
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

                j = JiebaTalk()
                jieba_contact_list = j.jiebala(Content)
                jieba_contact = json.loads(contact_list)
                contact_list = jieba_contact
                
                if contact_list:
                    contact = choice(contact_list)
                    contact = contact['content']
                    contactTalk = wxTpl % (FromUserName, ToUserName,CreateTime,MsgType,contact)
                    self.write(contactTalk)
                else:
                    #contact = smdmy
                    t = CreateTime
                    c = Talk()
                    contact =c.talk(t)
                    contactTalk = wxTpl % (FromUserName, ToUserName,CreateTime,MsgType,contact)
                    self.write(contactTalk)
        else:
                pass
        

goInterface = [
    (r"/1984", WXInterface),
]
