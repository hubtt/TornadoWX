#!/usr/bin/env python
<<<<<<< HEAD
# -*- coding: utf-8 -*-
#
#  未命名.py
#  
#  Copyright 2013 ccdjh <ccdjh@WD>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  



def main():
	
	return 0

if __name__ == '__main__':
	main()

=======
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

    def helper_config(self,name,value):
        pass
        
>>>>>>> origin/vps
