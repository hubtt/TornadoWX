#!/usr/bin/env python
# coding=utf-8
import os
import json
import lxml
import redis
import tornado.web

from helper import HelperHandler
from config import KT

class Main(HelperHandler):
    def get(self):
        kv = redis.StrictRedis()
        c = kv.get('xxxxxxxx')
        
        self.write(c)
        
        
class Weixin(HelperHandler):
    @tornado.web.authenticated
    def get(self):
        kv = redis.StrictRedis()
        g = self.get_argument('g', 'all')
        contact_list = []
        
        if g == 'all':
            contact_list_all = kv.keys(KT['c']+'*')#如果没有，返回[]
            for t in contact_list_all[0:30]:
                c = kv.get(t)
                c = json.loads(c)
                contact_list.append(c)
                
        
        
        template_values = {}
        template_values['WX'] = '模板变量全部用大写'
        template_values['CONTACT_LIST'] = contact_list
        self.render(os.path.join(os.path.dirname(__file__), 'template','weixin.html'),tpl=template_values)
        

class CreateContact(HelperHandler):
    def get(self):
        pass
    @tornado.web.authenticated
    def post(self):
        group_name = str(self.get_argument("groupName","hot").encode("UTF-8"))
        contact_name = str(self.get_argument("contactName",None).encode("UTF-8"))
        contact_content = str(self.get_argument("contactContent",None).encode("UTF-8"))

        kv = redis.StrictRedis()
        contact_key = str(KT['c']) + contact_name
        contact_value = {'name':contact_name,'content':contact_content,'list':[],}
        contact_value = json.dumps(contact_value)
        kv.set(contact_key, contact_value)#创建联系人
        self.redirect('/wx?g=' + group_name + "&s=" + contact_name)
        

class Settings(HelperHandler):
    def get(self):
        template_values = {}
        template_values['SETTINGS'] = '模板变量全部用大写'
        self.render(os.path.join(os.path.dirname(__file__), 'template','settings.html'),tpl=template_values)


goWX = [
    (r"/", Main),
    (r"/wx", Weixin),
    (r"/create/contact", CreateContact),
    (r"/settings", Settings),
]
