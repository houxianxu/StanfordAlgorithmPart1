"""
programming assignment 6b

The goal of this problem is to 
implement the "Median Maintenance" algorithm
"""

import heapq

lowHeap = [] # which is a maxHeap and use negative to accomplish
hightHeap = [] # which is a minHeap

def medianMaintenanceInsert(item):
	global lowHeap, hightHeap

	if len(lowHeap) == 0:
		heapq.heappush(lowHeap, -item)
	else:
		m = -lowHeap[0]
		if item > m:
			heapq.heappush(hightHeap, item)
			if len(hightHeap) > len(lowHeap):
				trans = heapq.heappop(hightHeap)
				heapq.heappush(lowHeap, -trans)
		else:
			heapq.heappush(lowHeap, -item)
			if len(lowHeap) - len(hightHeap) > 1:
				trans = -heapq.heappop(lowHeap)
				heapq.heappush(hightHeap, trans)


# test
# if __name__ == '__main__':
# 	medianMaintenanceInsert(4)
# 	medianMaintenanceInsert(3)
# 	medianMaintenanceInsert(2)
# 	medianMaintenanceInsert(1)
# 	medianMaintenanceInsert(0)

# 	print lowHeap, hightHeap


def main():
	medianSum = 0

	input_file = open('Median.txt')

	for line in input_file:

		item = int(line.strip())
		medianMaintenanceInsert(item)

		m = -lowHeap[0]
		# print lowHeap
		
		medianSum += m

	print medianSum % 10000

if __name__ == '__main__':
	main()




