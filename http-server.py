# -*- coding:utf-8 -*-

import time
import BaseHTTPServer
import logging

formatter = '%(asctime)s: %(message)s'

logger = logging.getLogger('test')
logger.handlers = []
con_handler = logging.StreamHandler()
con_handler.setFormatter(formatter)
logger.addHandler(con_handler)

class MyHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_HEAD(self):
		self.send_response(200)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):
		logger.info("get an request");
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		self.wfile.write("<html><head><title>gaia python demoe</title></head>")
		self.wfile.write("<body><p>this is a demo.</p>")
		self.wfile.write("<p>hello world V1.0R020.</p>")
		self.wfile.write("<p>hello world V1.0R070.</p>")
		self.wfile.write("<p>hello world tstack.global.com V1.0R020</p>")
		self.wfile.write("<p>测试环境，V1.0R050</p>")
		self.wfile.write("<p>You accessed path: %s</p>" % self.path)
		self.wfile.write("</body></html>")


def main():
	httpd = BaseHTTPServer.HTTPServer(('', 80), MyHandler)
	print time.asctime(), "Server Starts - %s:%s" % ('', 80)
	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	
	httpd.server_close()
	print time.asctime(), "Server Stops - %s:%s" % ('', 80)

if __name__ == '__main__':
	main()
