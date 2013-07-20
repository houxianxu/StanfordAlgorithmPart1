from quickSort import *

file_name = 'QuickSort.txt'
input_file = open(file_name, 'r')
dataList = []
for line in input_file:
	data = int(line.strip())
	dataList.append(data)
input_file.close()

# print dataList

count = 0
res = quickSort(dataList)
print res
