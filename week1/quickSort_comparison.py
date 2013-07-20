import random

comparisons = 0

def quickSort(array, left, right):
	if left < right:
		# pivotIndex = pickPivotFirstIndex(left, right)
		# pivotIndex = pickPivotLastIndex(left, right)
		pivotIndex = pickPivotMedianIndex(left, right)
		# pivotIndex = pickPivotRandomIndex(left, right)
		newPivotIndex = partition(array, left, right, pivotIndex)
		quickSort(array, left, newPivotIndex - 1)
		quickSort(array, newPivotIndex + 1, right)

def partition(array, left, right, pivotIndex):
	global comparisons

	comparisons += (right - left)

	pivot = array[pivotIndex]
	swap(array, left, pivotIndex)
	i = left + 1
	j = left + 1
	while j < len(array):
		if array[j] < pivot:
			swap(array, i, j)
			i += 1
		j += 1
	swap(array, left, i - 1)
	return i -1 

def pickPivotFirstIndex(left, right):
	return left

def pickPivotLastIndex(left, right):
	return right

def pickPivotMedianIndex(left, right):
	middle = (left + right) // 2
	if (array[left] > array[middle] and array[left] < array[right]) or \
		(array[left] < array[middle] and array[left] > array[right]):
		return left
	if (array[right] > array[middle] and array[right] < array[left]) or \
		(array[right] < array[middle] and array[right] > array[left]):
		return right
	else:
		return middle

def pickPivotRandomIndex(left, right):
	return random.randint(left, right)

def swap(array, i, j):
	temp = array[j]
	array[j] = array[i]
	array[i] = temp

def buildList(file_name):
	input_file = open(file_name, 'r')
	dataList = []
	for line in input_file:
		data = int(line.strip())
		dataList.append(data)
	input_file.close()
	return dataList

if __name__ == '__main__':
	array = buildList('QuickSort.txt')
	quickSort(array, 0, len(array) - 1)
	print comparisons
