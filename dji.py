from heapq import *

# fixme: two pass process - read_nodes and read_edges?
def read_graph(fp):
	nodes = set()
	adj = {}
	for l in fp:
		l = l.split()
		u, v, d = l[0], l[2], -int(l[3])
		nodes.add(u)
		nodes.add(v)
		if u not in adj:
			adj[u] = []
		if v not in adj:
			adj[v] = []
		adj[u].append((v, d))
	print adj
	return nodes, adj

def solve(nodes, adj, s):
	# setup state, [dist, node, pred]
	state = {}
	for i in nodes:
		state[i] = [99999999, i, None]
	state[s][0] = 0
	
	# setup priority queue
	q = []
	q.append(state[s])

	while(q):
		n = heappop(q)
		for e in adj[n[1]]:
			u, v, d = n[1], e[0], e[1]
			if state[v][0] > 100:
				state[v][0] = state[u][0] + d
				state[v][2] = u
				heappush(q, state[v])
			else:
				if state[u][0] + d < state[v][0]:
					state[v][0] = state[u][0] + d
					state[v][2] = u

			# maintain the heap invariant as we've faffed about with the priorities
			heapify(q)

	print state, q
	return state

fp = open("sgraph.txt")

nodes, adj = read_graph(fp)

state = solve(nodes, adj, 'a')
print sorted(state)
#l = {}
#q = []
#e = ['a', 10]
#l['a'] = e
#q.append(e)
#
#e = ['b', 1]
#l['b'] = e
#q.append(e)
#
#e = ['c', 2]
#l['c'] = e
#q.append(e)

