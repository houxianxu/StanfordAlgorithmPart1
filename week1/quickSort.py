from partition import *


def quickSort(L):
	begin = 0
	end = len(L) - 1
	res = qSort(L, begin, end)
	return res

def qSort(L, begin, end):
	"""	list of number -> list of number

	return a list of numbers which are sorted in 
	O(nlgn) time 
	>>> [4, 3, 5, 7]
	[3, 4, 5, 7]
	"""
	global count
	
	if begin < end:
		n = end - begin
		count += n
		mid = partition(L, begin, end)
		qSort(L, begin, mid-1)
		qSort(L, mid+1, end)
	return count


	



if __name__ == '__main__':
	print quickSort([4, 3, 5, 7, 6, -1])

