#!/usr/bin/env python

import os

def visit_func(arg, dirname, names):
	print 'visiting ' + dirname
	for i in names:
		print i

print 'calling walk'
os.path.walk('/home/brycek', visit_func, None)
