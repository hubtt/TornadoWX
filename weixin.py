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
        pass

class Weixin(HelperHandler):
    @tornado.web.authenticated
    def get(self):
        template_values = {}
        template_values['WX'] = '模板变量全部用大写'
        self.render(os.path.join(os.path.dirname(__file__), 'template','weixin.html'),tpl=template_values)
        
        
goWX = [
    (r"/", Main),
    (r"/wx", Weixin),
]
