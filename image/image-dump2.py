#!/usr/bin/env python

import os, sys
import Image

#filename = "220px-Lenna-blackness2.png"
filename = "imp_local.tga"

#def write_pixel(s, x, islast):
#	s += "\t{ %3i, %3i, %3i, %3i }" % x
#	s += "%s" % (",", "")[islast]
#
#def iterate_pixels(s, data, func):
#	for i in range(len(data)):
#		func(s, data[i], i == len(data) - 1)
#


#modes = { 'default':	['unsigned char', convert_default],
#	'float':	['float', convert_float]
#} 
	
def write_header(data):
	strlist = []
	for x in data:
		strlist.append("\t{ %3i, %3i, %3i, %3i }" % x)

	print ',\n'.join(strlist)


def write_header2(data):
	print ',\n'.join(["\t{ %3i, %3i, %3i, %3i }" % (x[0], x[1], x[2], x[3]) for x in data])

def str_func(x):
	return "\t{ %3i, %3i, %3i, %3i }" % (x[0], x[1], x[2], x[3])

def write_header3(data):
	print ',\n'.join(str_func(x) for x in data)

def write_header3(data):
	print ',\n'.join(map(str_func, data))

im = Image.open(filename)
data = list(im.getdata())

write_header3(data)

test = ["\t{ %3i, %3i, %3i, %3i }" % (x[0], x[1], x[2], x[3]) for x in data]

