def permute_string(s):
	flags = [False for i in range(len(s))]
	p = ""

	do_permute(s, flags, p, 0)

# done with generative recursion
# consumes a string and flags and a position, generates a character and calls the recursion
def do_permute(s, flags, p, i):
	if i == len(s):
		print p
	
	for j in range(len(s)):
		if flags[j] == True:
			continue
		flags[j] = True;
		do_permute(s, flags, p + s[j], i + 1)
		flags[j] = False;

def combination_string(s):
	do_combination(s, "", 0)

def do_combination(s, result, pos):
	if pos == len(s) - 1:
		print result

	print s[pos]

	for c in s[pos:]:
		do_combination(s, result + c, pos + 1)

combination_string("abcd")

	
