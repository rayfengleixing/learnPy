#!/usr/bin/env python
# -*- coding:utf-8 -*-

from tornado import web, httpserver, ioloop

class IndexHandler(web.RequestHandler):
	def get(self):
		self.write("Hello World!<br>")
		self.write("Web Test...")

application = web.Application([
		(r"/", IndexHandler),
	])

if __name__ == '__main__':
	http_server = httpserver.HTTPServer(application)
	http_server.listen(8080)
	ioloop.IOLoop.current().start()
