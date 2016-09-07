def parse_string(s):
	i = 0
	while True:
		if i == len(s):
			return
		elif s[i] == ' ':
			i += 1
		elif s[i] in ["([{"]:
			print "OPEN_PAREN"
			i += 1
		elif s[i] in ['0123456789']:
			print "NUM"
			i += 1
		elif s[i] == '+':
			print "OPERATOR_+"
			i += 1
			

