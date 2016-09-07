def print_number1(n):
	while n != 0:
		r = n % 10
		n = n / 10
		print r,

def print_number2(n):
	d = 100000
	while True:
		c = n / d
		n = n % d
		print c,

		if d == 1:
			break
		d = d / 10

print_number1(154)
print_number2(154)

