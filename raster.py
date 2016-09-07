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


from itertools import *

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
v2 = (0.0, 256.0)
edges = make_edges(v0, v1, v2)
draw_triangle(image, edges)

#v0 = (256.0, 256.0)
#v1 = (0.0, 256.0)
#v2 = (256.0, 0.0)
#edges = make_edges(v0, v1, v2)
#draw_triangle(image, edges)

write_ppm("raster.ppm", image, 256, 256)
    
