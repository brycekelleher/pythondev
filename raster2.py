from itertools import *
from math import *

def make_edges(v0, v1, v2):
	e0 = (v1[1] - v2[1], v2[0] - v1[0], (v1[0] * v2[1]) - (v2[0] * v1[1]))
	e1 = (v2[1] - v0[1], v0[0] - v2[0], (v2[0] * v0[1]) - (v0[0] * v2[1]))
	e2 = (v0[1] - v1[1], v1[0] - v0[0], (v0[0] * v1[1]) - (v1[0] * v0[1]))
	return (e0, e1, e2)

def edge_test(e, p):
	tedge = (e[0] == 0.0 and e[1] > 0.0)
	ledge = (e[0] > 0.0)
	dot = (e[0] * p[0]) + (e[1] * p[1]) + e[2]
	#print "dot", dot, "ledge", ledge, "tedge", tedge
	return dot > 0.0 or (dot == 0.0 and (tedge or ledge))
	#return dot >= 0.0

def tri_test(e, p):
	return all([edge_test(e[i], p) for i in range(3)])

def calculate_coeffs(det, edges, b0, b1, b2):
	a = edges[0][0] * b0 + edges[1][0] * b1 + edges[2][0] * b2
	b = edges[0][1] * b0 + edges[1][1] * b1 + edges[2][1] * b2
	c = edges[0][2] * b0 + edges[1][2] * b1 + edges[2][2] * b2
	a *= det
	b *= det
	c *= det
	return (a, b, c)

def calculate_layer(det, edges, b0, b1, b2, count):
	coeffs = []
	for i in range(count):
		coeffs.append(calculate_coeffs(det, edges, b0[i], b1[i], b2[i]))
	return coeffs

def interpolate_layer(coeffs, pixel):
	v = coeffs[0] * pixel[0] + coeffs[1] * pixel[1] + coeffs[2]
	v = max(0.0, min(v, 1.0))
	return v

def draw_triangle(image, e):
	rows = range(256)
	cols = range(256)
	pixels = product(rows, cols)
	for y, x in pixels:
		image[(x, y)] = image.get((x, y), [0, 0, 0])

		pixeladdr = ((float(x) + 0.5, float(y) + 0.5))
		lit = tri_test(e, pixeladdr)
		if lit:
			image[(x, y)][0] += 0.5
			image[(x, y)][1] += 0
			image[(x, y)][2] += 0

def checkerboard(u, v):
	u = int(floor(u * 10.0))
	v = int(floor(v * 10.0))
	polarity = (u & 1) ^ (v & 1)
	if polarity:
		return (1, 1, 1)
	else:
		return (0, 0, 0)

def draw_triangle2(image, e, c):
	rows = range(256)
	cols = range(256)
	pixels = product(rows, cols)
	for y, x in pixels:
		image[(x, y)] = image.get((x, y), [0, 0, 0])

		pixeladdr = ((float(x) + 0.5, float(y) + 0.5))
		lit = tri_test(e, pixeladdr)
		if lit:
			r = interpolate_layer(c[0], pixeladdr)
			g = interpolate_layer(c[1], pixeladdr)
			b = interpolate_layer(c[2], pixeladdr)
			image[(x, y)][0] += r
			image[(x, y)][1] += g
			image[(x, y)][2] += b

def draw_triangle3(image, e, c):
	rows = range(256)
	cols = range(256)
	pixels = product(rows, cols)
	for y, x in pixels:
		image[(x, y)] = image.get((x, y), [0, 0, 0])

		pixeladdr = ((float(x) + 0.5, float(y) + 0.5))
		lit = tri_test(e, pixeladdr)
		if lit:
			r = interpolate_layer(c[0], pixeladdr)
			g = interpolate_layer(c[1], pixeladdr)
			color = checkerboard(r, g)
			image[(x, y)][0] += color[0]
			image[(x, y)][1] += color[1]
			image[(x, y)][2] += color[2]

def write_ppm(filename, image, imagew, imageh):
	fp = open(filename, "w")
	fp.write("P3\n%i %i\n255\n" % (imagew, imageh))

	cols = range(imagew)
	rows = range(imageh)
	for y in rows:
		for x in cols:
			# convert from image space into sample space here (invert y)
			color = image[(x, imageh - 1 - y)]

			# 'tonemap' the colors
			r = int(255 * color[0])
			g = int(255 * color[1])
			b = int(255 * color[2])

			# write the pixel values to the ppm file
			fp.write("%i " % r)
			fp.write("%i " % g)
			fp.write("%i " % b)
			fp.write("\n")

image = {}

v0 = (0.0, 0.0)
v1 = (256.0, 0.0)
v2 = (128.0, 128.0)
red = (1.0, 0.0, 0.0)
green = (0.0, 1.0, 0.0)
blue = (0.0, 0.0, 1.0)
uv0 = (0.0, 1.0, 0.0)
uv1 = (1.0, 0.0, 0.0)
uv2 = (0.0, 0.0, 0.0)

edges = make_edges(v0, v1, v2)
det = 1.0 / (edges[0][2] + edges[1][2] + edges[2][2])
#coeffs = calculate_layer(det, red, green, blue, 3)
coeffs = calculate_layer(det, edges, uv0, uv1, uv2, 3)
draw_triangle3(image, edges, coeffs)

#v0 = (256.0, 256.0)
#v1 = (0.0, 256.0)
#v2 = (256.0, 0.0)
#edges = make_edges(v0, v1, v2)
#draw_triangle(image, edges)

write_ppm("raster.ppm", image, 256, 256)
    
