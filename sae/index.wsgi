#!/usr/bin/env python
# coding=utf-8
import os
import tornado.wsgi
import tornado.web
import sae

from weixin import goWX
from sign import goSign
from interface import goInterface

settings = {"cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=","login_url": "/signin"}

go = goWX+goSign+goInterface 
 
app = tornado.wsgi.WSGIApplication(go, **settings)
application = sae.create_wsgi_app(app)
