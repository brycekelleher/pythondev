from math import *

# would the data be better stored as a dict?
class vec3:
	def __init__(self, x, y, z):
		self.xyz = dict(zip([0, 1, 2], [x, y, z]))
	def __getitem__(self, key):
		return self.xyz[key]
	def __setitem__(self, key, item):
		self.xyz[key] = item
	#def __str__(self):
	#	return "(%f, %f, %f)" % (self.x, self.y, self.z)
	def __repr__(self):
		return "vec3(%f, %f, %f)" % (self.xyz[0], self.xyz[1], self.xyz[2])
	def __add__(self, other):
		return vec3(self.xyz[0] + other.xyz[0], self.xyz[1] + other.xyz[1], self.xyz[2] + other.xyz[2])
	def __sub__(self, other):
		return vec3(self.xyz[0] - other.xyz[0], self.xyz[1] - other.xyz[1], self.xyz[2] - other.xyz[2])
	def __mul__(self, other):
		return vec3(self.xyz[0] * other.xyz[0], self.xyz[1] * other.xyz[1], self.xyz[2] * other.xyz[2])
	def __rmul__(self, other):
		return vec3(other * self.xyz[0], other * self.xyz[1], other * self.xyz[2])

def add3(a, b):
	return (a[0] + b[0], a[1] + b[1], a[2] + b[2])
def sub3(a, b):
	return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def dot3(a, b):
	return (a[0] * b[0]) + (a[1] * b[1]) + (a[2] * b[2])
def cross3(a, b):
	return ((a[1] * b[2]) - (a[2] * b[1]), (a[2] * b[0]) - (a[0] * b[2]), (a[0] * b[1]) - (a[1] * b[0]));
def scalartriple(a, b, c):
	return dot3(a, cross3(b, c));
def length3(v):
	return sqrt((v[0] * v[0]) + (v[1] * v[1]) + (v[2] * v[2]))
def normalize3(v):
	return (1.0 / length3(v)) * v
