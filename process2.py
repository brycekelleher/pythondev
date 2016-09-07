import multiprocessing

class QueueProcess(multiprocessing.Process):
	def __init__(self):
		self.q = multiprocessing.Queue()
		super(QueueProcess, self).__init__(name='queue_class_process')
	
	def run(self):
		while True:
			s = self.q.get()
			print 'read \'{}\' from the queue'.format(s)
			if s == 'exit':
				print 'got exit token'
				#return
	def put(self, x):
		self.q.put(x)
		

if __name__ == '__main__':
	p = QueueProcess()
	p.start()
	for s in "the cat sat on the mat exit".split():
		p.put(s)
	p.join()

