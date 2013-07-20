import time
from count_and_merge_sort import *

file_name = 'IntegerArray.txt'
input_file = open(file_name, 'r')

dataList = []

for line in input_file:
	data = int(line.strip())
	dataList.append(data)
input_file.close()

# print dataList

# dataList = [5, 4, 3, 2, 1]
# count = 0
# for i in xrange(len(dataList)):
# 	for j in xrange(i+1, len(dataList)):
# 		if dataList[i] > dataList[j]:
# 			count += 1
# print count

# the result: 2407905288 by previous brute force algorithm
start_time = time.time()
res = count_and_merge_sort(dataList)
print res[0]
print time.time() - start_time

