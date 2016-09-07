from math import *
from random import *
from itertools import *

def radi(n, base):
	val = 0
	invbase = 1.0 / base
	invbi = invbase

	while n > 0:
		val += (n % base) * invbi
		n /= base
		invbi *= invbase

	return float(val)

def sample_list(n):
	return [(i / float(n), radi(i, 2)) for i in range(n)]

def perm_sample_list(n):
	x = sample(range(n), n)
	return [(i / float(n), radi(x[i], 2)) for i in range(n)]
	
# uniform sample hemisphere
def ushemi(u1, u2):
	r = sqrt(1.0 - u1 * u1);
	phi = 2.0 * 3.141592653 * u2;
	return (r * cos(phi), r * sin(phi), u1)

# cosine sample hemisphere
def cshemi(u1, u2):
	r = sqrt(u1);
	theta = 2 * 3.141592653 * u2;
	return  (r * cos(theta), r * sin(theta), sqrt(1.0 - u1))

import pylab

def plot_samples(s):
	x, y = zip(*s)
	pylab.plot(x, y, '.')
	pylab.show()

from mpl_toolkits.mplot3d import Axes3D

def plot_ushemi(n):
	s = sample_list(n)
	v = [ushemi(i[0], i[1]) for i in s]
	x, y, z = zip(*v)

	fig = pylab.figure()
	ax = fig.add_subplot(111, projection='3d')
	ax.scatter(x, y, z, c='r', marker='o')
	ax.set_xlabel('X Label')
	ax.set_ylabel('Y Label')
	ax.set_zlabel('Z Label')

	pylab.show()

#s = sample_list(1024)
#plot_samples(s)

#s = perm_sample_list(1024)
#plot_samples(s)

#plot_ushemi(256)

# estimate pi using monte carlo
def run_montecarlo(n):
	samples = sample_list(n)
	incircle = 0
	for i in samples:
		l = sqrt((i[0] * i[0]) + (i[1] * i[1]))
		if l < 1.0: incircle += 1
	return n, incircle

# code to estimate the integral x^2 from 0 to 4 f(x)=x^2 and p(x) is the uniform distribution 1 / 4.0
def estimate_integral():
	s = sample_list(4096)
	x, y = zip(*s)
	y = [(i * 4) ** 2 for i in x]
	return (4.0 / len(x)) * sum(y)

def estimate_integral2():
	# function to be integrated
	def f(x): return x ** 2
	# probability density function for uniform sampled variable
	def p(x): return (1 / 4.0)
	
	s = sample_list(4096)
	x, y = zip(*s)

	y = [f(i * 4) / p(x) for i in x]
	return (1.0 / len(x)) * sum(y)

#print estimate_integral2()

def print_samples(n):
	print reduce(lambda r, i: r + "{}, {}\n".format(i[0], i[1]), s, "")

