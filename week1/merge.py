def merge(list1, list2):
	""" (list1 of num, list2 of num) -> list of num

	Return a sorted list contains all the item 
	in list1 and list2

	Precondition: list1 and list2 are sorted

	>>> merge([1, 2, 6], [3, 4, 7])
	[1, 2, 3, 4, 6, 7]
	"""

	res = []

	i = 0
	j = 0
	# compare the item in both lists, the get the smaller
	# in res
	while i <= len(list1)-1 and j <= len(list2)-1:
		if list1[i] < list2[j]:
			res.append(list1[i])
			i += 1
		else:
			res.append(list2[j])
			j += 1

	while i <= len(list1)-1:
		res.append(list1[i])
		i += 1

	while j <= len(list2)-1:
		res.append(list2[j])
		j += 1

	return res

if __name__ == '__main__':
	print(merge([1, 2, 6], [3, 4, 7]))



