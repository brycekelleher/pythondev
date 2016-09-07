import sys, os, time

def print_loop1():
	for i in sys.stdin.read():
		if i == '\n':
			sys.stdout.write('\r\n')
			continue
		sys.stdout.write(i)
		time.sleep(0)

def print_loop2():
	for i in sys.stdin.read():
		if i == '\n':
			sys.stdout.write('\r\n')
			continue
		c = chr(ord(i) + 1)
		sys.stdout.write(c)
		time.sleep(0)

def main_loop():
	cpid = os.fork()
	if cpid == 0:
		print_loop2()
	else:
		print_loop1()
		os.waitpid(-1, 0)

main_loop()

