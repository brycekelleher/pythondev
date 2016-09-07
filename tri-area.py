#! /usr/bin/python

v0 = (1, 0, 0)
v1 = (0, 1, 0)
v2 = (-1, 0, 0)

def tri_area(v0, v1, v2):
	return ((v1[0] - v0[0]) * (v2[0] - v0[0]) + (v1[1] - v0[1]) * (v2[1] - v0[1]) + (v1[2] - v0[2]) * (v2[2] - v0[2]))

def volume(v0, v1, v2):
	det = 0

	det += (v0[0] * v1[1] * v2[2])
	det += (v1[0] * v2[1] * v0[2])
	det += (v2[0] * v0[1] * v1[2])
	det -= (v2[0] * v1[1] * v0[2])
	det -= (v1[0] * v0[1] * v2[2])
	det -= (v0[0] * v2[1] * v1[2])

	return det

print "area: %f" % (tri_area(v0, v2, v1))
print "volume: %f" % (volume(v0, v1, v2))


