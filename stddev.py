def mean(x):
	return sum(x) / len(x)

def stddev(x):
    m = mean(x)
    return (sum([(i - m) ** 2 for i in x]) / len(x)) ** 0.5

l0 = [0,1,2,3,4,5,6,7,8]
l1 = [5,10,10,10,15]
l2 = [0,1,2,4,6,8]
l3 = [6,7,11,12,13,15]
l4 = [9,0,0,3,3,3,6,6]

print "l0", mean(l0), stddev(l0)
print "l1", mean(l1), stddev(l1)
print "l2", mean(l2), stddev(l2)
print "l3", mean(l3), stddev(l3)
print "l4", mean(l4), stddev(l4)
