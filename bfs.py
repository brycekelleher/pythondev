#!/usr/bin/python

from collections import deque

size = (4, 4)
nodes = {}

def isvalid(xy):
	# bounds check
	if (xy[0] < 0) or (xy[1] < 0):
		return False
	if (xy[0] >= size[0]) or (xy[1] >= size[1]):
		return False
	return True

def makenode(xy):
	return { 'xy': xy, 'pred': None }

def getnode(xy):
	if not isvalid(xy):
		return None
	if not xy in nodes:
		nodes[xy] = makenode(xy)
	return nodes[xy]

def adjnode(i, xy):
	if i == 0: return (xy[0] + 1, xy[1]    )
	if i == 1: return (xy[0]    , xy[1] + 1)
	if i == 2: return (xy[0] - 1, xy[1]    )
	if i == 3: return (xy[0]    , xy[1] - 1)

def adjnode2(i, xy):
	if i == 0: return (xy[0] + 1, xy[1]    )
	if i == 1: return (xy[0] + 1, xy[1] + 1)
	if i == 2: return (xy[0]    , xy[1] + 1)
	if i == 3: return (xy[0] - 1, xy[1] + 1)
	if i == 4: return (xy[0] - 1, xy[1]    )
	if i == 5: return (xy[0] - 1, xy[1] - 1)
	if i == 6: return (xy[0]    , xy[1] - 1)
	if i == 7: return (xy[0] + 1, xy[1] - 1)

# search the graph from source(s) to target(t)
def search(s, t):
	queue = deque()
	queue.append((s, s))

	while len(queue):
		q = queue.popleft()
		xy = q[0]

		# don't process invalid nodes or nodes which have already been seen
		n = getnode(xy)
		if not n:
			continue
		if not n['pred'] == None:
			continue
		n['pred'] = q[1]

		# if this is the target node then break
		if xy == t:
			break

		# walk to the adjcent nodes
		for i in range(4):
			adj = adjnode2(i, n['xy'])
			queue.append((adj, n['xy']))

# walk backwards from the target
def constructpath(t):
	n = nodes[t]
	while True: 
		print n['xy']
		if n['xy'] == n['pred']:
			break
		n = nodes[n['pred']]

def main():
	search((0, 0), (2, 3))
	constructpath((2, 3))
main()
