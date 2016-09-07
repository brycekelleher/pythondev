def ba(a, b, i, j):
	if i == len(a) and j == len(b):
		return 0

	cost = 99999
	if i < len(a) and j < len(b) and a[i] == b[j]:
		cost = min(cost, 0 + ba(a, b, i + 1, j + 1))
	if i < len(a):
		cost = min(cost, 1 + ba(a, b, i + 1, j))
	if j < len(b):
		cost = min(cost, 1 + ba(a, b, i, j + 1))

	return cost

print ba('snowy', 'sunny', 0, 0)
