def fib(n):
	if n < 2:
		return n
	else:
		return fib(n - 1) + fib(n - 2)

memo = {}
def fib_memo(n):
	if n in memo:
		return memo[n]
	if n < 2:
		f = n
	else:
		f = fib_memo(n - 1) + fib_memo(n - 2)

	memo[n] = f
	return f

print "fib(10):", fib(10)
print "fib_memo(100):", fib_memo(100)
