## read in a dictionary of words and put all the words in a hash table
## keyed on the sorted letter order

def init_table():
	global table
	table = {}

	fp = open('words')
	for l in fp:
		l = l.strip().lower()
		key = ''.join(sorted(l))
		entry = table.get(key, [])
		entry.append(l)
		#table[key] = entry

def anagrams(table, word):
	key = ''.join(sorted(word))
	print table[key]

## driver
import sys

def map_anagrams(word):
	global table
	anagrams(table, word)

def main():
	init_table()
	map(map_anagrams, sys.argv[1:])

if __name__ == '__main__':
	main()
