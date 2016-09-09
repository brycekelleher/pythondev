from itertools import product, dropwhile
from math import sqrt

def read_map():
	fp = open('map')
	w, h = map(int, fp.readline().split())
	cells = [(x, y) for y, x in product(range(w), range(h))]

	data = [i for i in fp.read() if i in '.xsg']
	return w, h, dict(zip(cells, data))

def is_passable(i, mapdata):
	return mapdata[i] != 'x'

def is_valid_cell(cell, w, h):
	x, y = cell
	return x >= 0 and y >= 0 and x < w and y < h

def startcell(mapdata):
	return list(dropwhile(lambda x: mapdata[x] != 's', mapdata.keys()))[0]

def goalcell(mapdata):
	return list(dropwhile(lambda x: mapdata[x] != 'g', mapdata.keys()))[0]

def build_cell_edge_list(w, h, mapdata, cell):
	x, y = cell
	edges = []
	dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

	# build a list of neighbours
	n = [(x + dx, y + dy) for dx, dy in dirs]

	# filter the list for valid neighbours
	n = [i for i in n if is_valid_cell(i, w, h) and is_passable(i, mapdata)]

	# build the edge list (fixme: can combine with previous line)
	edges = [(i, 1.0) for i in n]

	return edges

def build_edges(w, h, mapdata):
	# fixme: can build list of edges for each cell and zip to create dict
	edges = {}
	for k in mapdata.keys():
		edges[k] = build_cell_edge_list(w, h, mapdata, k)
	return edges

def build_graph():
	global edges, w, h, mapdata
	w, h, mapdata = read_map()

	edges = build_edges(w, h, mapdata)

	return { 'w': w, 'h': h, 'mapdata': mapdata, 'edges': edges }

def draw_output(w, h, mapdata, route):
	cells = product(range(w), range(h))
	output = ""
	for y in range(h):
		for x in range(w):
			if (x, y) in route:
				output += '*'
			else:
				output += mapdata[(x, y)]
		output += "\n"
	print output

def find_route_breadth_first(start, goal):
	q = [[start]]
	enq_count = 0

	while True:
		#print 'q', q
		# pop a path from the queue
		path = q.pop(0)

		# check if we've reached the goal
		if path[0] == goal:
			print 'found route:', path, enq_count
			return path

		# extend the paths
		edges = graph['edges'][path[0]]
		for node, distance in edges:

			# don't bite our own tail
			if node in path:
				continue

			# don't enqueue if another path has already been through this node
			if any([node in p for p in q]):
				continue

			#q.insert(0, [node] + path)
			q.append([node] + path)
			enq_count += 1

def cell_distance(a, b):
	ax, ay = a
	bx, by = b
	return sqrt(((bx - ax) ** 2) + ((by - ay) ** 2))

def find_route_best_first(start, goal):
	q = [[start]]
	enq_count = 0
	ext_count = 0
	bestgoalpath = None

	while len(q) > 0:
		# pop a path from the queue
		argmin = min(range(len(q)), key=lambda x: cell_distance(q[x][0], goal))
		path = q.pop(argmin)

		# check if we've reached the goal
		if path[0] == goal:
			print 'found route:', path, enq_count, ext_count
			if bestgoalpath == None or len(path) < len(bestgoalpath):
				bestgoalpath = path
				continue

		# (bound) don't extend if this path is longer than a path already found to the goal
		if bestgoalpath != None and len(path) > len(bestgoalpath):
			#print 'culled path', path
			continue

		# extend the paths
		edges = graph['edges'][path[0]]
		for node, distance in edges:
			ext_count += 1

			# don't bite our own tail
			if node in path:
				continue

			# don't enqueue if another path has already been through this node
			if any([node in p for p in q]):
				continue

			#q.insert(0, [node] + path)
			q.append([node] + path)
			enq_count += 1

	return bestgoalpath

def find_route(start, goal):
	return find_route_best_first(start, goal)

if __name__ == '__main__':
	read_map()

	global graph
	graph = build_graph()

	scell = startcell(mapdata)
	gcell = goalcell(mapdata)
	print scell, gcell
	path = find_route(scell, gcell)

	draw_output(w, h, mapdata, path)

