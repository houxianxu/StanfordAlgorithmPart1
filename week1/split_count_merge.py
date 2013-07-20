def split_count_merge(list1, list2):
	"""(list, list) -> [int, list]

	Return a list which the first element is the
	inverstion from the first list to the second one.
	And the second one the merge list of two

	Precondtion: list1 and list2 are sorted 

	>>> split_count_merge([3, 5, 6], [4, 7, 8])
	[2, [3, 4, 5, 6, 7, 8]]
	"""

	length1 = len(list1)
	length2 = len(list2)

	i, j = 0, 0
	res = [0, []]

	while (i <= length1 - 1) and (j <= length2 - 1):
		if list1[i] <= list2[j]:
			res[1].append(list1[i])
			i += 1
		else:
			res[1].append(list2[j])
			res[0] += length1 - i
			j += 1

	if i <= length1 - 1:
		res[1].extend(list1[i:])
		

	if j <= length2 - 1:
		res[1].extend(list2[j:])


	return res

if __name__ == '__main__':
	print split_count_merge([8, 9, 10], [4, 7, 8])