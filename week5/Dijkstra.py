"""
programming assignment 5

code up Dijkstra's shortest-path algorithm. 
"""
import heapq
def buildAdjList(file_name):
	""" file -> list of list1, list of list2

	Return a list of list of lists, which represent a undirect graph.

	the index of the list is the number of the vertex
	and the value of the according index is the adjacent vertex

	example: 
			[[[100, 2], [1000, 3]], [[10000, 6], [100000, 7]]] -> the 0 vertex has edges to 2, 3 vertex,
											 and the weight is 100 and 1000 respectively
										   the 1 vertex has edges to 6, 7 vertex, and the weith is 10000
										   and 100000 respectively.

	"""
	input_file = open(file_name, 'r')
	adjList = []

	for line in input_file:
		# calculate the vertex and one adjacent vertex accordingly
		data = line.strip().split()
		adjList.append([])
		
		# print data
		vertexFrom = int(data[0]) - 1

		for vertexAndWeight in data[1:]:
			dataList = vertexAndWeight.split(',')
			vertexTo = int(dataList[0]) - 1
			weight = int(dataList[1])
			adjList[vertexFrom].append((weight, vertexTo))

	return adjList

# test
# if __name__ == '__main__':
# 	print buildAdjList('test.txt')
# test

def dijkstra(graph, source):
	infinity = 100000000000
	n = len(graph)
	distance = {}

	for vertex in range(n):
		distance[vertex] = infinity
	distance[0] = 0

	visited = []

	queue = [] 

	for i in range(n):
		queue.append((distance[vertex], i))

	heapq.heapify(queue)

	while len(queue) > 0:
		d, u = heapq.heappop(queue)
		
		if u in visited:
			continue

		for data in graph[u]:
			v = data[1]
			weight = data[0]
			# print 'v-> ', v
			# print 'weight-> ', weight

			if distance[v] > (distance[u] + weight):	

				queue.remove((distance[v], v))

				distance[v] = distance[u] + weight
				queue.append((distance[v], v))
			
		heapq.heapify(queue)
		visited.append(u)

	return distance


def main():
	graph = buildAdjList('test.txt')
	# print graph

	distance = dijkstra(graph, 0)
	# print distance

	reqiured = [7,37,59,82,99,115,133,165,188,197]

	res = []
	for v in reqiured:
		v = v - 1
		res.append(distance[v])

	print ','.join(map(str, res))

if __name__ == '__main__':
	main()


