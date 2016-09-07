def level_dim(level):
	return 2 ** level

def level_size(level):
	return 4 ** level

def level_sum(level):
	if level == 0:
		return level_size(0)

	return level_size(level) + level_size(level - 1)

def level_offset(level):
	if level == 0:
		return 0

	return level_sum(level - 1)

def generate_quadtree_data():
	numlevels = 16
	d = [level_dim(i) for i in range(numlevels)]
	s = [level_size(i) for i in range(numlevels)]
	o = [level_offset(i) for i in range(numlevels)]

	return (d, s, o)

def print_array(a):
	print ", ".join(map(str, a))

d, s, o = generate_quadtree_data()

#print d
#print s
#print o
print_array(d)
print_array(s)
print_array(o)

# code to interleave the data
z = zip(d, s, o)
print ",\n".join(map(lambda e: "{ %i %i %i }" % e, z))

