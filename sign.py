#!/usr/bin/env python
# coding=utf-8
import os
import hashlib
import json
import lxml
import sae.kvdb as redis
import tornado.web

from helper import HelperHandler
from config import KT
from config import WXPassword


class Signin(HelperHandler):
    def get(self):
        template_values = {}
        self.render(os.path.join(os.path.dirname(__file__), 'template','sign.html'),tpl=template_values)
        
    def post(self):
        pw = self.get_argument("password")
        sha1 = hashlib.sha1(pw).hexdigest()
        if (sha1 == WXPassword):
            WXAuth = hashlib.sha1(WXPassword + ':' + 'WXSiteDomain').hexdigest()
            self.set_secure_cookie("user", WXAuth, expires_days=30)
            self.redirect('/wx')
        else:
            self.redirect('/signin')

class Signout(HelperHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect('/signin')


        
goSign = [
    (r"/signin", Signin),
    (r"/signout", Signout),
]
