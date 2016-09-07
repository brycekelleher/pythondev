#!/usr/bin/env python

import os, sys
import Image

def split_image(filename):
	im = Image.open(filename)

	yuv = im.convert("YCbCr")
	y, u, v	= yuv.split()

	f, e = os.path.splitext(filename)

	y.save(f + '-y' + ".bmp")
	u.save(f + '-u' + ".bmp")
	v.save(f + '-v' + ".bmp")

def main():
	for arg in sys.argv[1:]:
		split_image(arg)

main()

