# consumes an array and returns the sort order of elements
def quicksort(a):
	if len(a) <= 1:
		return a
	
	a, pivot = a[:-1], a[-1]
	lo = quicksort([i for i in a if i <= pivot])
	hi = quicksort([i for i in a if i >  pivot])
	return lo + [pivot] + hi

print quicksort([5, 7, 2, 9, 3, 1, 6])


## partition a into two sets, one that is less than the pivot
## and one that is greater than the pivot
## then put the pivot in the middle of the two sets
## invariant: 0:i less than, i:k greater than
def quicksort_partition(a, lo, hi):
	pivot = a[-1]
	j = 0
	for i in range(len(a) - 1):
		if a[i] <= pivot:
			a[j], a[i] = a[i], a[j]
			j += 1
	
	a[j], a[-1] = a[-1], a[j]
	return j

def quicksort_inplace_r(a, lo, hi):
	if hi - lo <= 1:
		return

	pivot = quicksort_partition(a, lo, hi)
	quicksort_inplace_r(a, 0, pivot - 1)
	quicksort_inplace_r(a, 0, pivot + 1)

def quicksort_inplace(a):
	quicksort_inplace_r(a, 0, len(a) - 1)

a = [5, 7, 2, 9, 3, 1, 6]
print a, quicksort_partition(a, 0, 6), a

quicksort_inplace(a)
print a
