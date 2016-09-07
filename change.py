#!/usr/bin/python
import sys

#counting leaf nodes is the number of ways to make change
def change(amount):
	if amount == 0:
		return 1

	count = 0
	if amount >= 50:
		count += change(amount - 50)
	if amount >= 20:
		count += change(amount - 20)
	if amount >= 10:
		count += change(amount - 10)

	return count

def minchange(amount):
	# making change for 0 requires 0 coins
	if amount == 0:
		return 0

	c = 1 + minchange(amount - 1)
	if amount >= 2:
		c = min(c, 1 + minchange(amount - 2))
	if amount >= 5:
		c = min(c, 1 + minchange(amount - 5))

	return c
		
def minchange_bu(amount):

	counts = {}
	counts[0] = 0
	counts[1] = 1
	counts[2] = 1
	counts[5] = 1

	for i in range(amount):
		c = 1 + counts[amount - 1]
		if amount >= 2:
			c = min(c, 1 + counts[amount - 2])
		if amount >= 5:
			c = min(c, 1 + counts[amount - 5])

	return counts[amount]
		

def main():
	print "change", change(int(sys.argv[1]))
	print "minchange", minchange(int(sys.argv[1]))
	print "minchange_bu", minchange(int(sys.argv[1]))

main()
