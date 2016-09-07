from itertools import product
from plane2d import *

imagew = 256
imageh = 256

rows = range(imagew)
cols = range(imageh)
pixels = product(rows, cols)

v0 = (0.2, 0.4)
v1 = (0.8, 0.2)
v2 = (0.5, 0.8)
abc0 = plane2d(v1, v0)
abc1 = plane2d(v2, v1)
abc2 = plane2d(v0, v2)

def clamp(x):
	return max(-1.0, min(x, 1.0))

# distance field
def df(xy):
	#transform to 0..1 space
	xx, yy = xy
	xx = xx / float(imagew)
	yy = yy / float(imageh)
	xy = (xx, yy)

	f0 = distance(abc0, xy)
	f1 = distance(abc1, xy)
	f2 = distance(abc2, xy)
	return max(f0, f1, f2)


def pixelfunc(xy):
	d = df(xy)
	f = df(xy)

	# bias, scale and clamp
	#f = 0.5 + 0.5 * f
	f = clamp(f)
	
	r = max(0.0,  f) * 256
	g = 0
	b = max(0.0, -f) * 256

	return (r, g, b)

print "P3"
print "256 256"
print "255"
for y  in rows:
	for x in cols:
		xy = x, y
		r, g, b = pixelfunc((xy))
		print int(r), int(g), int(b),
	print ""
