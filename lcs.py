#!/usr/bin/python

import sys

def lcs(a, b, i, j):
	if i == len(a) or j == len(b):
		return 0
	
	if a[i] == b[j]:
		return 1 + lcs(a, b, i + 1, j + 1)
	else:
		return max(lcs(a, b, i + 1, j), lcs(a, b, i, j + 1))

def main():
	l = lcs(sys.argv[1], sys.argv[2], 0, 0)
	print "lcs:", l

main()

