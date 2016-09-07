#!/usr/bin/env python

import os, sys
import Image

#filename = "220px-Lenna-blackness2.png"
#filename = "imp_local.tga"
filename = ""

def pixel_to_string_byte(x):
	return "%3i, %3i, %3i, %3i" % (x[0], x[1], x[1], x[2])

def pixel_to_string_float(x):
	f = (x[0] / 255.0, x[1] / 255.0, x[2] / 255.0, x[3] / 255)
	return "%1.6f, %1.6f, %1.6f, %1.6f" % (f[0], f[1], f[2], f[3])

def write_datatype(datatype, numpixels):
	print "%s imagedata[%i][4] =\n{" % (datatype, numpixels)

def write_data(data, pixel_to_string):
	print ',\n'.join(["\t{ %s }" % (pixel_to_string(x)) for x in data])

def write_end():
	print '}\n\n'

def write_header(mode, data):
	modes = {
		'byte':		['unsigned char', pixel_to_string_byte ],
		'float':	['float', pixel_to_string_float ]
	}

	datatype = modes[mode][0]
	pixelfunc = modes[mode][1]

	#write the header
	write_datatype(datatype, len(data))
	write_data(data, pixelfunc)
	write_end()

def main():
	mode = sys.argv[1]
	filename = sys.argv[2]

	im = Image.open(filename)
	data = list(im.getdata())

	write_header(mode, data)

main()
