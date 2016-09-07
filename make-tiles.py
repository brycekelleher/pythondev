from PIL import Image

tilew = 64
tileh = 64
imagew = 256
imageh = 256

tiles = [(x, y) for y in range(imageh / tileh) for x in range(imagew / tilew)]

for i, t in enumerate(tiles):
	coords = (t[0] * tilew, t[1] * tileh, (t[0] + 1) * tilew, (t[1] + 1) * tileh)
	filename = "imp_local_tile" + str(i) + ".tga"
	print i, coords, filename

	im = Image.open("imp_local.tga")
	croppedim = im.crop(coords)
	croppedim.save(filename)
