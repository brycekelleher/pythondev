visited = []
count = {}
move = {}

def lcs2(a, b):
	# there is no commmon substring between the empty string and any non-null string
	if a == "" or b == "":
		count[(a, b)] = 0
		move[(a, b)] = 'n'
		return
	
	if (a, b) in visited:
		return
	visited.append((a, b))

	# check for a match
	if a[0] == b[0]:
		lcs2(a[1:], b[1:])
		count[(a, b)] = 1 + count[(a[1:], b[1:])]
		move[(a, b)] = 'm'
		return 
	
	# choose which move to make
	lcs2(a[1:], b)
	lcs2(a, b[1:])

	count[(a, b)] = count[(a[1:], b)]
	move[(a, b)] = 'l'

	if count[(a, b[1:])] > count[(a[1:], b)]:
		count[(a, b)] = count[(a, b[1:])]
		move[(a, b)] = 'r'

def lcs_trace(a, b):
	common = []
	moves = []
	i, j = 0, 0
	state = (a[i:], b[i:])
	while(move[state] != 'n'):
		moves.append(move[state])
		if move[state] == 'm':
			common.append(a[i])
			i += 1
			j += 1
		elif move[state] == 'l':
			i += 1	
		else:
			j += 1

		state = (a[i:], b[j:])
	return common, moves

def print_aligned(a, b, moves):
	s = ""
	i = 0
	for m in moves:
		if m == 'm':
			s += a[i]
			i += 1
		elif m == 'l':
			s += a[i]
			i += 1
		else:
			s += '-'
	print s

	s = ""
	j = 0
	for m in moves:
		if m == 'm':
			s += b[j]
			j += 1
		elif m == 'r':
			s += b[j]
			j += 1
		else:
			s += '-'
	print s

def lcs_top(a, b):
	lcs2(a, b)
	common, moves = lcs_trace(a, b)
	#print visited
	#print count
	#print move
	print common
	print moves
	print_aligned(a, b, moves)

import sys
a = "cat"
b = "bat"
#lcs_top(a, b)
if len(sys.argv) > 1:
	lcs_top(sys.argv[1], sys.argv[2])

