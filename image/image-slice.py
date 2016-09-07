#!/usr/bin/env python

import os, sys
import Image

filename = "220px-Lenna.png"

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
	

def is_last_element(x, data):
	return data.index(x) == len(data) - 1

def write_header(data):
	s = ''

	s += "unsigned char imagedata[%i][%i] = {\n" % (len(data), 4)

	for x in data:
		s += "\t{ %3i, %3i, %3i, %3i }" % x

		if not is_last_element(x, data):
			s += ','

		s += "\n";

	s += "};\n"

	print s

def write_header(data):
	s = ''

	s += "unsigned char imagedata[%i][%i] = {\n" % (len(data), 4)

	for x in data:
		s += "\t{ %f, %f, %f, %f }" % (x[0] / 255.0, x[1] / 255.0, x[2] / 255.0, x[3] / 255.0)

		if not is_last_element(x, data):
			s += ','

		s += "\n";

	s += "};\n"

	print s

im = Image.open(filename)
crop = im.crop((0, 0, im.size[0], 1))
data = list(crop.getdata())

write_header(data)



