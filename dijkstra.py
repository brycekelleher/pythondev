def swap(a, i, j):
	a[i], a[j] = a[j], a[i]

#def upheap(a, i):
#	while (i > 0) and (a[i] < a[(i - 1) / 2]):
#		swap(a, (i - 1) / 2, i)
#		i = (i - 1) / 2

#enforce the invariant that the parent is less than the child at position i
def lessthan(a, b):
	return a < b

def upheap(a, i):
	while (i > 0):
		parent = (i - 1) / 2
		if (a[parent] < a[i]):
			break
		swap(a, parent, i)
		i = parent

def downheap(a, i):
	end = len(a)
	l = i * 2 + 1
	while (l < end):
		r = l + 1
		if (r < end) and (a[r] <  a[l]):
			l = r
		swap(a, i, l)
		i = l
		l = i * 2 + 1

def heappush(heap,nodes, x):
	heap.append(x)
	upheap(heap, len(a) - 1)

def heappop(a):
	x = a[0]
	a[0] = a.pop()
	downheap(a, 0)

nodes = [5, 7, 4, 2, 3, 1]
heap = []
for i in range(len(nodes)):
	heappush(
