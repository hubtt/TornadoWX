#!/usr/bin/env python
# coding=utf-8
import os
import hashlib
import json
import lxml
import redis
import tornado.web

from helper import HelperHandler
from config import KT
#>>> import hashlib
#>>> hashlib.sha1('123456').hexdigest()
#'7c4a8d09ca3762af61e59520943dc26494f8941b'
SinaPassword = '7c4a8d09ca3762af61e59520943dc26494f8941b'

class Signin(HelperHandler):
    def get(self):
        template_values = {}
        self.render(os.path.join(os.path.dirname(__file__), 'template','sign.html'),tpl=template_values)
        
    def post(self):
        pw = self.get_argument("password")
        sha1 = hashlib.sha1(pw).hexdigest()
        if (sha1 == SinaPassword):
            SinaAuth = hashlib.sha1(SinaPassword + ':' + 'SinaSiteDomain').hexdigest()
            self.set_secure_cookie("user", SinaAuth, expires_days=30)
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
