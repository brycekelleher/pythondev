# d - current cost, distance to get to this node from the start node
# o - operation performed to get to this node from the previous node
# p - the previous node
def align(a, b):
	d = {}
	o = {}
	p = {}
	for i in range(len(a) + 1):
		d[(i, 0)] = i
		o[(i, 0)] = 'd'
		p[(i, 0)] = (i - 1, 0)
	for j in range(len(b) + 1):
		d[(0, j)] = j
		o[(0, j)] = 'i'
		p[(0, j)] = (0, j - 1)

	for i in range(1, len(a) + 1):
		for j in range(1, len(b) + 1):
			cell = (i, j)
			d[cell] = 9999999

			prev = (i - 1, j - 1)
			if a[i-1:i] == b[j-1:j]:
				d[cell] = d[prev]
				o[cell] = 'm'
				p[cell] = prev

			prev = (i - 1, j)
			if d[prev] + 1 < d[cell]:
				d[cell] = d[prev] + 1
				o[cell] = 'd'
				p[cell] = prev

			prev = (i, j - 1)
			if d[prev] + 1 < d[cell]:
				d[cell] = d[prev] + 1
				o[cell] = 'i'
				p[cell] = prev
	return d, o, p

def pd(x, a, b):
	for i in range(len(a) + 1):
		for j in range(len(b) + 1):
			print x[(i, j)],
		print ""

def trace_back(o, p, cell):
	if cell == (0, 0):
		return
	
	trace_back(o, p, p[cell])
	print o[cell]

def trace_back2(o, p, cell):
	trace = []
	while cell != (0, 0):
		trace += [o[cell]]
		cell = p[cell]
	return list(reversed(trace))

def print_align(a, b, trace):
	i = 0
	s = ""
	for  t in trace:
		if t == 'm':
			s += a[i]
			i += 1
		elif t == 'i':
			s += '-'
		elif t == 'd':
			s += a[i]
			i += 1
	print s

	i = 0
	s = ""
	for  t in trace:
		if t == 'm':
			s += b[i]
			i += 1
		elif t == 'i':
			s += b[i]
			i += 1
		elif t == 'd':
			s += '-'
	print s

import sys
#a = 'snowy'
#b = 'sunny'
a = 'the cat sat on the mat'
b = 'the cat sat with a hat on the mat'
d, o, p = align(a, b)
#pd(d, a, b)
#pd(o, a, b)
#pd(p, a, b)
#trace_back(o, p, (len(a), len(b)))
trace = trace_back2(o, p, (len(a), len(b)))
print_align(a, b, trace)
if len(sys.argv) > 1:
	a = sys.argv[1]
	b = sys.argv[2]
	d, o, p = align(a, b)
	trace = trace_back2(o, p, (len(a), len(b)))
	print_align(a, b, trace)
