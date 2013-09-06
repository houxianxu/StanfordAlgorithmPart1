"""
programming assignment 6-1

implement a variant of the 2-SUM algorithm 

However, my implementation is very slow, it takes 1h on my PC to get the right answer!
"""


def buildArray(file_name):

	input_file = open(file_name, 'r')

	positive = []
	negative = []

	for line in input_file:
		line = int(line.strip())
		if line >=0:
			positive.append(line)
		else:
			negative.append(line)

	return positive, negative

# if __name__ == '__main__':
	# print buildArray('algo1_programming_prob_2sum.txt')




# use merge sort to sort the array which is just read from file

# def binarySearch(alist, item):

#    found = False
#    last = len(alist) - 1
#    first = 0

#    while first <= last and not found:
#    	midpoint = (first + last) // 2

#    	if alist[midpoint] == item:
#    		found = True
#    	else:

#    		if item < alist[midpoint]:
#    			last = midpoint - 1
#    		else:
#    			first = midpoint + 1
#    return found

# if __name__ == '__main__':
# 	alist = [1, 2, 3, 4,453, 5656, 65463]
# 	found = binarySearch(alist, 2)
# 	print found


def hashTable(alist):
	table = {}

	for i in alist:
		table[i] = True

	return table


def searchHashTable(hashTable, item):
	found = False

	if item in hashTable:
		found = True

	return found

# array = buildArray('algo1_programming_prob_2sum.txt')
# testhashTable = hashTable(array)
# for t in xrange(-10000, 10001):
# 	print 't-> ', t
# 	if 2000000 in testhashTable:
# 		print 'ture'


def main():
	positive, negative = buildArray('algo1_programming_prob_2sum.txt')

	# print array
	# arraySorted = merge_sort(arraydef numTwoSum(file_name):

	# print arraySorted
	negativeHashTable = hashTable(negative)
	negativeMin = min(negativeHashTable)
	negativeMax = max(negativeHashTable)
	# print negativeHashTable
	

	count = 0

	for t in xrange(-10000, 10001):
		print 't-> ', t

		for x in positive:
			y = t - x

			if (y < negativeMin) or y > negativeMax:
				print 'break'
				break
		
			found = searchHashTable(negativeHashTable, y)

			if found and (x != y):
				count += 1
				break

	print count
	
if __name__ == '__main__':

	main()
	










        



