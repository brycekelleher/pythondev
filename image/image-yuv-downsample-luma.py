#!/usr/bin/env python

import os, sys
import Image

def split_image(filename):
	im = Image.open(filename)

	yuv = im.convert("YCbCr")
	y, u, v	= yuv.split()

	# downsample the y component then rescale it to the u and v planes
	y = y.resize((y.size[0] / 2, y.size[1] / 2), Image.BICUBIC)
	y = y.resize((y.size[0] * 2, y.size[1] * 2), Image.NEAREST)

	im = Image.merge("YCbCr", (y, u, v))
	im = im.convert("RGB")

	f, e = os.path.splitext(filename)

	im.save(f + '-downsampled-luma' + e)

def main():
	for arg in sys.argv[1:]:
		split_image(arg)

main()

