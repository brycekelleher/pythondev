#list -> number
# return the maximum element in a
def maxlist(a):
	if len(a) == 1:
		return a[0]
	else:
		return max(a[0], maxlist(a[1:]))

#list -> number
def argmax(a, i, j):
	if (a[i] >= a[j]):
		return i
	else:
		return j

def argmaxlist(a, i, j):
	if i == j:
		return i
	else:
		return argmax(a, i, argmaxlist(a, i + 1, j))


l = [1, 5, 9, 4]
print maxlist(l)
print argmaxlist(l, 0, len(l) - 1)
