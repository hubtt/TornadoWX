#!/usr/bin/env python
# coding=utf-8
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
from weixin import goWX
from sign import goSign


define("port", default=8888, help="run on the given port", type=int)
settings = {"static_path": os.path.join(os.path.dirname(__file__), "static"),"debug": True,"cookie_secret": "61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=","login_url": "/signin"}
goFavicon = [(r"/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path=settings['static_path']))]

go = goFavicon+goWX+goSign
def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application(go,**settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
