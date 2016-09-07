def genSublists(L, n):
	r = []
	for i in range(0, len(L) - n + 1):
		r.append(L[i:i + n])
	return r

L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print genSublists(L, 4)

def longest_increasing_subarray(L):
	state = {}
	state[0] = 1
	for i in range(1, len(L)):
		if L[i] > L[i - 1]:
			state[i] = state[i - 1] + 1
		else:
			state[i] = 1
	return max(state.values())
			
L = [10, 4, 6, 8, 3, 4, 5, 7, 7, 2]
print longest_increasing_subarray(L)
