def normalized_area(f, b, o,):
	t = float(sum(f + b + o))
	f = sum(f)
	b = sum(b)
	o = 1.0 - f - b

	return [ f / t, b / t, o / t]

from random import choice, sample

f = sample(range(0, 10), 5)
b = sample(range(0, 10), 5)
o = sample(range(0, 10), 5)
print normalized_area(f, b, o)
