import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		#print 'Message received from {0}:\n{1}\n'.format(self.request.remote_ip, message)
		print self.request
		self.write("Hello, world")

class TestHandler(tornado.web.RequestHandler):
	def get(self):
		#print 'Message received from {0}:\n{1}\n'.format(self.request.remote_ip, message)
		print self.request
		self.write("This is the test handler")

def make_app():
	return tornado.web.Application([ (r"/", MainHandler), (r"/test", TestHandler)])

if __name__ == "__main__":
	app = make_app()
	app.listen(8888)
	tornado.ioloop.IOLoop.current().start()
