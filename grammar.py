from random import choice

grammar = {
'S': [['NP','VP']],
'NP': [['ART', 'N']],
'VP':  [['V', 'NP']],
'ART': ['the', 'a'],
'N': ['man', 'ball', 'woman', 'table'],
'V': ['hit', 'took', 'saw', 'liked'],
'N': ['man', 'ball', 'woman', 'table']
}

#for each entry in the rule evalulate it
def evalrule(rule):
	symbol = choice(rule)

	if not isinstance(symbol, list):
		return [symbol]

	result = []
	for s in symbol:
		result.append(generate(s))

	return result

def generate(symbol = 'S'):
	return evalrule(grammar[symbol])
