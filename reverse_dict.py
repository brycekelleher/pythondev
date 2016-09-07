def reverse_dict(d):
	r = {}
	for k in d:
		v = d[k]
		if v not in r.keys():
			r[v] = []
		r[v].append(k)
		r[v] = sorted(r[v])
	return r

test = {1:10, 2:20, 3:30}
print reverse_dict(test)

test = {4:True, 2:True, 0:True}
print reverse_dict(test)

