# coding=utf-8

import sys
reload(sys) 
sys.setdefaultencoding('utf-8')

import tornado.wsgi
import sae
import tornado.httpserver
import tornado.ioloop
import tornado.options

import os.path
import tornado.web
from tornado.httpclient import AsyncHTTPClient


class indexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')


application = tornado.web.Application([
	(r"/", indexHandler)
],  static_path=os.path.join(os.path.dirname(__file__), "static"),
	template_path=os.path.join(os.path.dirname(__file__), "template"),
	debug = True)




