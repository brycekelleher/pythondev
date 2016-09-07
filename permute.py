#!/usr/bin/python

from random import *

def swap(l, i, j):
	tmp = l[i]
	l[i] = l[j]
	l[j] = tmp

def permute(l):
	n = len(l)
	for i in range(n):
		r = randint(i, n - 1)
		swap(l, i, r)

l = range(10)
print l
print permute(l)
print l
