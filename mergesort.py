def merge(a, b):
	r = []
	i = j = 0
	while i < len(a) and j < len(b):
		if a[i] < b[j]:
			r.append(a[i])
			i += 1
		else:
			r.append(b[j])
			j += 1
	while i < len(a):
		r.append(a[i])
		i += 1
	while j < len(b):
		r.append(b[j])
		j += 1
	return r



def mergesort(l):
	# conquer
	if len(l) == 1:
		return l
	
	# divide
	mid = len(l) / 2
	lo = mergesort(l[:mid])
	hi = mergesort(l[mid:])

	# combine
	return merge(lo, hi)

print mergesort([5, 3, 8, 2, 1, 7, 6])
print mergesort([5, 3, 8, 2, 1, 7, 6, 4])

