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

def genrandomnum():
	# sample a uniform distribution
	r = random()

	# sample a normal distribution, scale and bias and then clamp
	r = normalvariate(0.0, 0.2)
	r = 0.5 + 0.5 * r
	r = min(max(0.2, r), 0.8)

	return r

def splitrects(F):
	i = choosenextsplit(F)
	if isrectsmall(F[i]):
		return F
	w, h, = F[i]['w'], F[i]['h']


	if w > h:
		f1, f2 = splitrectv(F[i], int(f * w))
	else:
		f1, f2 = splitrecth(F[i], int(f * h))

	# build the new list with F[i] sliced out and f1 and f2 inserted
	F = F[:i] + F[i + 1:] + [f1] + [f2]
	return splitrects(F)

def splitrects2(F):
	result = []
	queue = F[:]

	while(len(queue) > 0):
		f = queue.pop(0)

		if isrectsmall(f):
			result.append(f)
		else:
			w, h, = f['w'], f['h']
			r = genrandomnum()
			if w > h:
				f1, f2 = splitrectv(f, int(r * w))
			else:
				f1, f2 = splitrecth(f, int(r * h))
			queue += [f1, f2]

	return result

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

	F = splitrects2(F)
	drawrects(F)
