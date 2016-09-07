import cairo
from random import random, seed, uniform, normalvariate

WIDTH, HEIGHT = 16, 16


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

""" perform a veertical split """
def splitrectv(f, pos):
	f1 = {}
	f1['x'] = f['x']
	f1['y'] = f['y']
	f1['w'] = pos
	f1['h'] = f['h']

	f2 = {}
	f2['x'] = f['x'] + pos
	f2['y'] = f['y']
	f2['w'] = f['w'] - pos
	f2['h'] = f['h']

	return f1, f2

""" perform a veertical split """
def splitrecth(f, pos):
	f1 = {}
	f1['x'] = f['x']
	f1['y'] = f['y']
	f1['w'] = f['w']
	f1['h'] = pos

	f2 = {}
	f2['x'] = f['x']
	f2['y'] = f['y'] + pos
	f2['w'] = f['w']
	f2['h'] = f['h'] - pos

	return f1, f2

def choosenextsplit(F):
	return max(range(len(F)), key=lambda x: F[x]['w'] * F[x]['h'])

def isrectsmall(f):
	if f['w'] < 4:
		return True
	if f['h'] < 4:
		return True
	if f['w'] * f['h'] < 16:
		return True

	return False

""" consumes a rectangle and produces a list of split rectangles """
def splitrects(f):
	if isrectsmall(f):
		return [f]

	w, h, = f['w'], f['h']
	rnum = random()
	rnum = min(max(0.0, normalvariate(0.0, 0.2)), 1.0)
	rnum = 1.0 - rnum
	if w > h:
		f1, f2 = splitrectv(f, int(rnum * w))
	else:
		f1, f2 = splitrecth(f, int(rnum * h))

	F1 = splitrects(f1)
	F2 = splitrects(f2)
	return F1 + F2

def drawrects(R):

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
	F = [{ 'x': 0, 'y': 0, 'w': WIDTH, 'h': HEIGHT }]

	F = splitrects(F[0])
	drawrects(F)
