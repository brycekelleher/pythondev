import numpy as np
dot = np.dot
inv = np.linalg.inv
transpose = np.transpose
hstack = np.hstack
cat = np.concatenate
zero = np.array([0, 0, 0])

r = np.identity(3)
t = np.array([[1, 0, 3], [0, 1, 4], [0, 0, 1]])
m = dot(r, t)

a0 = [1, 1, 1]
a1 = [2, 4, 1]
a2 = [1, 2, 1]
a3 = [5, 7, 1]
a4 = [3, 8, 1]
a = np.array([
	hstack((a0, zero, zero)), 
	hstack((a1, zero, zero)), 
	hstack((a2, zero, zero)), 
	hstack((a3, zero, zero)), 
	hstack((a4, zero, zero)), 
	hstack((zero, a0, zero)), 
	hstack((zero, a1, zero)), 
	hstack((zero, a2, zero)), 
	hstack((zero, a3, zero)), 
	hstack((zero, a4, zero)), 
	hstack((zero, zero, a0)), 
	hstack((zero, zero, a1)), 
	hstack((zero, zero, a2)), 
	hstack((zero, zero, a3)), 
	hstack((zero, zero, a4))])

b0 = dot(m, a0)
b1 = dot(m, a1)
b2 = dot(m, a2)
b3 = dot(m, a3)
b4 = dot(m, a4)
b = transpose(np.array([b0[0], b1[0], b2[0], b3[0], b4[0], b0[1], b1[1], b2[1], b3[1], b4[1], b0[2], b1[2], b2[2], b3[2], b4[2]]))

#solve the overdetermined system using least squares
atrans = transpose(a)
asquare = dot(atrans, a)
x = dot(dot(inv(dot(transpose(a), a)), transpose(a)), b)


