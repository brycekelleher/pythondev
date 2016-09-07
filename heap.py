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

def upheap2(a, i, compare):
	while (i > 0):
		parent = (i - 1) / 2
		if compare(a[parent], a[i]):
			break
		swap(a, parent, i)
		i = parent

def downheap2(a, i):
	end = len(a)
	l = i * 2 + 1
	while (l < end):
		r = l + 1
		if (r < end) and compare(a[r], a[l]):
			l = r
		swap(a, i, l)
		i = l
		l = i * 2 + 1

def downheap3(a, i):
	end = len(a)
	while(i < end / 2):
		j = i * 2 + 1
		if (j + 1 < end) and (a[j + 1] < a[j]):
			j = j + 1
		if (a[i] < a[j]):
			break
		swap(a, i, j)

def heappush(a, x):
	a.append(x)
	upheap(a, len(a) - 1)

def heappop(a):
	if len(a) == 1:
		return a.pop()

	x = a[0]
	a[0] = a.pop()
	downheap3(a, 0)
	return x

h = []
heappush(h, 3)
heappush(h, 5)
heappush(h, 8)
heappush(h, 6)
heappush(h, 7)

