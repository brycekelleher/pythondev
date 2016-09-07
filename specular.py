from pylab import *

def func_blinn(x):
	x = x + 0.0000001
	x2 = x ** 2
	return min(4.0, (1.0 / (3.1415 * x2)) * x * ((2.0 / x2) - 2.0))

def func_ggx(x, alpha):
	alpha2 = alpha ** 2
	x2 = x ** 2
	return 3.1415 * ((x2 * (alpha2 - 1.0) + 1.0) ** 2)


x = [i / 1000.0 for i in range(1000)]
blinn = [func_blinn(i) for i in x]
ggx = [func_ggx(i, 0.006) for i in x]

plot(x, blinn)
plot(x, ggx)
show()
