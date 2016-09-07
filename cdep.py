#!/usr/bin/python
import sys
import os

def read_file(filename):
	try:
		f = open(filename, 'r')
		return f.read().lower()
	except IOError:
		print "Error opening or reading input file:", filename
		sys.exit()

def parse_includes(filename):
	data = read_file(filename)
	data = data.replace("\"", " ")
	data = data.replace("<", " ")
	data = data.replace(">", " ")
	tokens = data.split()
	itr = iter(tokens)
	for t in itr:
		if t == "#include":
			print "\"" + os.path.basename(filename) + "\"", "->", "\"" + next(itr) + "\""

def walk_files(root):
	exts = ['.cpp', '.c', '.h']
	for root, dirs, files in os.walk(root):
		for f in files:
			if f.endswith(".c") or f.endswith(".cpp") or f.endswith(".h"):
				#print "processing: ", os.path.join(root, f)
				parse_includes(os.path.join(root, f))
				

def main():
	print "digraph test"
	print "{"
	walk_files(sys.argv[1])
	print "}"

main()
