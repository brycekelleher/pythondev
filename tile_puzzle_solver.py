from itertools import product

board_w = 3
board_h = 3
rows = range(0, board_h)
cols = range(0, board_w)
squares = list(product(rows, cols))
values = [str(i) for i in range(1, 9)]
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
sb = dict(zip(squares, [str(i) for i in range(1, 9)] + ['.']))

def read_initial_state(f):
	data = [i for i in f.read() if i.isdigit() or i == '.'] 
	b = dict(zip(squares, data))
	e = squares[data.index('.')]
	return (b, e)

def new_move(x, m):
	return (x[0] + m[0], x[1] + m[1])

def square_valid(x):
	if x[0] < 0 or x[0] >= board_h:
		return False
	if x[1] < 0 or x[1] >= board_w:
		return False
	return True

def swap_squares(b, x, y):
	nb = dict(zip(b.keys(), [b[i] for i in b.keys()]))
	tmp = nb[x]
	nb[x] = nb[y]
	nb[y] = tmp
	return (nb, y)

def board_state_list(b):
	return [b[i] for i in squares]

def is_solved(b):
	return all([i[0] == i[1] for i in zip(values, board_state_list(b))])

def solve(state):
	stack = []
	visited = []
	stack.append(state)
	while(len(stack)):
		state = stack.pop(0)
		if state in visited:
			continue
		visited.append(state)

		b, e = state[0], state[1]

		if is_solved(b):
			print b
			return

		validmoves = filter(square_valid, [new_move(e, i) for i in moves])
		#print "e", e, "validmoves", validmoves
		for m in validmoves:
			nb, ne = swap_squares(b, e, m)
			print "nb", nb, "ne", ne
			stack.append((nb, ne))

def solve_ids_internal(state, depthlimit):
	stack = []
	visited = []
	b, e = state[0], state[1]
	stack.append((b, e, 0))
	while(len(stack)):
		state = stack.pop()
		b, e, d = state[0], state[1], state[2]

		if d == depthlimit:
			return

		if b in visited:
			continue
		visited.append(b)

		if is_solved(b):
			print b
			return

		validmoves = filter(square_valid, [new_move(e, i) for i in moves])
		#print "e", e, "validmoves", validmoves
		for m in validmoves:
			nb, ne = swap_squares(b, e, m)
			print "nb", nb, "ne", ne
			stack.append((nb, ne, d + 1))

def solve_ids(state):
	for i in range(0, 1000):
		solve_ids_internal(state, i)

#f = open("tile_state_solved")
#f = open("tile_state_easy")
#f = open("tile_state_medium")
f = open("tile_initial_state")
b, e = read_initial_state(f)
print b
solve_ids((b, e))
