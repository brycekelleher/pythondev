def rod_cut(n):
	cuts = [1, 2, 3]
	prices = dict(zip(cuts, [1, 5, 8]))

	profit = {}
	moves = {}
	profit[0] = 0
	moves[0] = 0

	for i in range(1, n + 1):
		# evaluate the moves we can make and pick the best one
		profit[i] = 0
		for j in cuts:
			# filter out moves we can't make
			if i - j < 0:
				continue

			# calculate the profit we'll make for this move
			p = profit[i - j] + prices[j]

			if p > profit[i]:
				profit[i] = p
				moves[i] = j
	
	print " ".join([str((i, profit[i], moves[i])) for i in range(n + 1)])

	# trace the cuts back
	i = n
	trace = []
	while i != 0:
		trace.append(moves[i])
		i -= moves[i]
	print list(reversed(trace))

def rod_cut2(n):
	cuts = [1, 2, 3]
	prices = dict(zip(cuts, [1, 5, 8]))

	profit = {}
	moves = {}
	numcuts = {}
	profit[0] = 0
	moves[0] = 0
	numcuts[0] = 0

	for i in range(1, n + 1):
		# evaluate the moves we can make and pick the best one
		profit[i] = -9999999
		for j in cuts:
			# filter out moves we can't make
			if i - j < 0:
				continue

			# calculate the profit we'll make for this move
			p = profit[i - j] + prices[j] - (numcuts[i - j] + 1)

			if p > profit[i]:
				profit[i] = p
				moves[i] = j
				numcuts[i] = numcuts[i - j] + 1
	
	print " ".join([str((i, profit[i], moves[i], numcuts[i])) for i in range(n + 1)])

	# trace the cuts back
	i = n
	trace = []
	while i != 0:
		trace.append(moves[i])
		i -= moves[i]
	print list(reversed(trace))

rod_cut2(10)
