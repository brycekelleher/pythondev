from itertools import takewhile

program = "(+ 2 2)"

def issymbol(s):
	return all(not str.isspace(i) and i != ')' and i != '(' for i in s)

def parse_symbol(program):
	sym = "".join(takewhile(issymbol, program))
	return sym, len(sym)

def lisp_tokenize(program):
	tokens = []
	while len(program):
		if str.isspace(program[0]):
			program = program[1:]
		elif program[0] == '(':
			tokens.append('(')
			program = program[1:]
		elif program[0] == ')':
			tokens.append(')')
			program = program[1:]
		else:
			s, l = parse_symbol(program)
			tokens.append(s)
			program = program[l:]

	print 'tokens', tokens
	return tokens

def lisp_syntax(tokens):
	print tokens
	while len(tokens):
		if tokens[0] == '(':
			tokens = tokens[1:]

			expr = []
			while tokens[0] != ')':
				i, tokens = lisp_syntax(tokens)
				expr.append(i)

			#strip the trailing ')'
			tokens = tokens[1:]
			return expr, tokens
		else:
			return tokens[0], tokens[1:]


def lisp_parse(program):
	expr = lisp_syntax(lisp_tokenize(program))
	print 'expr', expr
	#return lisp_syntax(lisp_tokenize(program))

def lisp_eval(program):
	pass

lisp_eval(lisp_parse(program))
