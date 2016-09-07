#!/usr/bin/env python

import os, sys
import Image

def downsample_chroma(filename, factor):
	im = Image.open(filename)

	yuv = im.convert("YCbCr")
	y, u, v	= yuv.split()

	# downsample the chroma components then rescale it to back to y
	u = u.resize((u.size[0] / factor, u.size[1] / factor), Image.BICUBIC)
	u = u.resize((y.size[0], y.size[1]), Image.NEAREST)

	v = v.resize((v.size[0] / factor, v.size[1] / factor), Image.BICUBIC)
	v = v.resize((y.size[0], y.size[1]), Image.NEAREST)

	im = Image.merge("YCbCr", (y, u, v))
	im = im.convert("RGB")

	f, e = os.path.splitext(filename)

	im.save(f + '-downsampled-chroma-' + str(factor) + e)
	u.save('u-test' + e)
	v.save('v-test' + e)

def main():
	for arg in sys.argv[1:]:
		downsample_chroma(arg, 2)
		downsample_chroma(arg, 4)

main()

