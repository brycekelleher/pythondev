towers = { 0: ["d", "c", "b", "a"], 1: [], 2: [] }

def move_single_disk(towers, srctower, dsttower):
	val = towers[srctower].pop()

	if len(towers[dsttower]) > 0 and ord(val) > ord(min(towers[dsttower])):
		print "invalid move!"

	towers[dsttower].append(val)
	print "move {} from {} to {}".format(val, srctower, dsttower)

def move_disks(towers, n, srctower, dsttower, buftower):
	if n == 0:
		move_single_disk(towers, srctower, dsttower)
	else:
		move_disks(towers, n - 1, srctower, buftower, dsttower)
		move_single_disk(towers, srctower, dsttower)
		move_disks(towers, n - 1, buftower, dsttower, srctower)

move_disks(towers, 3, 0, 2, 1)

