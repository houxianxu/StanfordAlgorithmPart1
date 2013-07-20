def partition(L, begin, end):
	""" (list of numbers), int, int -> int

	return the position of the pivot
	side effect: put the pivot in the right position
	>>> partition([4, 3, 5], 0, 2)
	1
	"""
	##
	temp = L[end]
	L[end] = L[begin]
	L[begin] = temp
	##
	p = L[begin]
	i = begin + 1
	for j in xrange(begin+1, end+1):
		if L[j] < p:
			temp = L[j]
			L[j] = L[i]
			L[i] = temp
			i += 1
	L[begin] = L[i-1]
	L[i-1] = p
	return i-1

if __name__ == '__main__':
	L = [4, 3, 5, 9, -1]
	print partition(L, 0, 4)
	print L


