def ed(a, b):
	tabl = {}
	pred = {}
	op = {}

	#initialize the base cases that are only dependent on one predecessor node
	tabl[(0, 0)] = 0
	pred[(0, 0)] = (0, 0)
	op[(0, 0)] = '0'
	for i in range(1, len(b) + 1):
		tabl[(i, 0)] = tabl[(i - 1, 0)] + 1
		pred[(i, 0)] = (i - 1, 0)
		op[(i, 0)] = 'i'
	for j in range(1, len(a) + 1):
		tabl[(0, j)] = tabl[(0, j - 1)] + 1
		pred[(0, j)] = (0, j - 1)
		op[(0, j)] = 'd'
	
	# evaluate the nodes in the dag
	for i in range(1, len(a) + 1):
		for j in range(1, len(b) + 1):

			tabl[(i, j)] = 999999999

			# can we get to this state with a match? if so it costs nothing
			if (a[i - 1] == b[j - 1]):
				tabl[(i, j)] = tabl[(i - 1, j - 1)]
				pred[(i, j)] = (i - 1, j - 1)
				op[(i, j)] = 'm'
				continue

			#evaluate the delete operation
			if (tabl[(i - 1, j)] + 1 < tabl[(i, j)]):
				tabl[(i, j)] = tabl[(i - 1, j)] + 1
				pred[(i, j)] = (i - 1, j)
				op[(i, j)] = 'd'

			#evaluate the insert operation
			if (tabl[(i, j - 1)] + 1 < tabl[(i, j)]):
				tabl[(i, j)] = tabl[(i, j - 1)] + 1
				pred[(i, j)] = (i, j - 1)
				op[(i, j)] = 'i'

			#evaluate the replace operation
			if (tabl[(i - 1, j - 1)] + 1 < tabl[(i, j)]):
				tabl[(i, j)] = tabl[(i - 1, j - 1)] + 1
				pred[(i, j)] = (i - 1, j - 1)
				op[(i, j)] = 'r'

	for i in range(len(a) + 1):
		for j in range(len(b) + 1):
			print tabl[(i, j)],
		print ""
	for i in range(len(a) + 1):
		for j in range(len(b) + 1):
			print pred[(i, j)],
		print ""
	# could get rid of this by looking at predecessor difference and cost difference
	for i in range(len(a) + 1):
		for j in range(len(b) + 1):
			print op[(i, j)],
		print ""

ed("cat", "dog")
ed("sunny", "snowy")
