import sys

def lis(seq):
	pred = [None for x in range(len(seq))]
	length = [1 for x in range(len(seq))]
	#iterate through each node in the dag
	for i in range(len(seq)):
		#visit each incoming edge to this graph node
		for j in range(i):
			if (seq[j] < seq[i]) and (length[j] + 1 > length[i]):
				length[i] = length[j] + 1
				pred[i] = j
		print length, pred

lis(map(int, sys.argv[1:]))
