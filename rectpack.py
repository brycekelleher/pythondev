import cairo
from random import random, seed

def findbestempty(rw, rh, F):
	# implementation of first fit
	for i, f in enumerate(F):
		if rw <= f['w'] and rh <= f['h']:
			return i

	# couldn't find a fit
	return None

def splitrect(f, rw, rh):
	r = {}
	r['w'] = rw
	r['h'] = rh
	r['x'] = f['x']
	r['y'] = f['y']

	# choose which axis to split
	f1 = {}
	f1['w'] = r['w']
	f1['h'] = f['h'] - rh
	f1['x'] = f['x']
	f1['y'] = f['y'] + rh

	f2 = {}
	f2['w'] = f['w'] - rw
	f2['h'] = f['h']
	f2['x'] = f['x'] + rw
	f2['y'] = f['y']

	return r, f1, f2

def packrect(R, F, rw, rh):
	i = findbestempty(rw, rh, F)
	r, f1, f2 = splitrect(F[i], rw, rh)
	return (R + [r], F[:i] + F[i + 1:] + [f1] + [f2])

def drawrects(R):

	WIDTH, HEIGHT = 16, 16

	surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
	ctx = cairo.Context (surface)

	#ctx.scale (WIDTH, HEIGHT) # Normalizing the canvas

	seed(0)
	for r in R:
		ctx.rectangle(r['x'], r['y'], r['w'], r['h'])
		ctx.set_source_rgb(random(), random(), random())
		ctx.fill()

	surface.write_to_png ("example.png") # Output to PNG


if __name__ == '__main__':
	R = []
	F = [{ 'x': 0, 'y': 0, 'w': 16, 'h': 16 }]

	#rlist = [(2, 3), (2, 2), (2, 5)]
	rlist = [(2, 3), (2, 2), (4, 5), (2, 5), (6, 7), (4, 2), (3, 6)]
	for rw, rh in rlist:
		R, F = packrect(R, F, rw, rh)

	print R
	drawrects(R)
	
