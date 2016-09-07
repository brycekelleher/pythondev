class node:
	def __init__(self, k):
		self.l = None
		self.r = None
		self.k = k
	def __repr__(self):
		return str(("k", self.k, "l", self.l, "r", self.r))

def bst_insert(root, k):
	if root == None:
		return node(k)
	
	n = root
	while(n):
		if k < n.k:
			if n.l == None:
				n.l = node(k)
				return root
			else:
				n = n.l
		else:
			if n.r == None:
				n.r = node(k)
				return root
			else:
				n = n.r
	
def bst_insert2(root, k):
	if root == None:
		return node(k)
	
	p, n = None, root
	while(n):
		p = n
		if k < n.k:
			n = n.l
		else:
			n = n.r

	if k < p.k:
		p.l = node(k)
		return root
	else:
		p.r = node(k)
		return root

def bst_min(n):
	while n.l != None:
		n = n.l
	return n.k

def bst_successor(r, k):
	# find the node
	n = r
	trace = []
	while n.k != k:
		trace.append(n)
		if k < n.k:
			n = n.l
		else:
			n = n.r
	trace.append(n)

	# return min if n has has a right sub tree
	if n.r != None:
		return bst_min(n.r)
	else:
		# walk through the trace looking for the successor
		# this will be the first r child link
		i = len(trace) - 1
		j = i - 1
		while i > 0:
			if trace[i] == trace[j].l:
				return trace[j].k
			i = j
			j -= 1
		return None

def bst_build_tree(l):
	t = None
	for i in l:
		t = bst_insert2(t, i)
	return t

def bst_print(n):
	if n == None:
		return
	bst_print(n.l)
	print n.k,
	bst_print(n.r)

n = node(3)
n = bst_insert(n, 5)
n = bst_insert(n, 1)
print (n)

from random import choice, sample
l = sample(range(50), 20)
n = bst_build_tree(l)
bst_print(n)
bst_successor(n, choice(l))
