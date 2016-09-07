import multiprocessing

def f(q):
	while True:
		s = q.get()

		#guard clause
		if s == 'exit':
			print 'got exit token'
			#return

		print 'read \'{}\' from the queue'.format(s)


if __name__ == '__main__':
	q = multiprocessing.Queue()
	p = multiprocessing.Process(target=f, name='queue_process', args=(q,))
	p.start()
	for s in "the cat sat on the mat exit".split():
		q.put(s)
	p.join()

