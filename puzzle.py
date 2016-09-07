from itertools import combinations, permutations, chain
s = "lelqgauin"

# generate a list of all possible permutations
l = chain(*[permutations(s, i) for i in range(len(s))])

#filter everything that doesn't contain g
l = [i for i in l if 'g' in i]

for i in l:
	print '^' + ''.join(i) + '$'

