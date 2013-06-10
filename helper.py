#!/usr/bin/env python
# coding=utf-8
import hashlib
import redis
import tornado.web

class HelperHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        return self.get_secure_cookie("user")
            
    def helper_counter(self,name):
        """Returns Python objects for the given counter."""
        c = name
        #kv = sae.kvdb.KVClient() #在SinaAppEngine时候使用
        kv = redis.StrictRedis()  #在vps时候使用
        counter = kv.get(c)
        if counter is None:
                kv.set(c, 1)
                num = 1
                return num
        else:
                num = int(counter) + 1
                kv.set(c, num)
                return num
