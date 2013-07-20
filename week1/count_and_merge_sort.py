from split_count_merge import *


def count_and_merge_sort(L):

	""" (list of number) -> int

	Return the number of inversion of a list using
	mergeSort using nlogn time
	>>> [4, 3, 2, 1]
	[6, [1, 2, 3, 4]]
	"""
	n = len(L)
	if n == 0 or n == 1:
		return [0, L]

	mid = len(L) / 2

	# both numbers are in left list
	LeftRes = count_and_merge_sort(L[: mid])
	leftCount = LeftRes[0]
	leftList = LeftRes[1]

	# both numbers are in right list
	rightRes = count_and_merge_sort(L[mid:])
	rightCount = rightRes[0]
	rightList = rightRes[1]

	# one is in the left and the other in right
	# here we use another function to count

	splitRes = split_count_merge(leftList, rightList)
	splitCount = splitRes[0]
	mergeList = splitRes[1]

	return [leftCount + rightCount + splitCount, mergeList]

if __name__ == '__main__':
	print count_and_merge_sort([4, 3, 2, 1])