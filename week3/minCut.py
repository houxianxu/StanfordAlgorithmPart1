import random
import copy
def buildAdjList(file_name):
	""" file -> list of list

	Return a list of list, which represent a graph.

	e.g. [[[vertex], [vertexAdj]], ...]
	"""
	input_file = open(file_name, 'r')
	adjList = []
	for line in input_file:
		data = map(int, line.strip().split())
		vertex = [data[0]]
		vertexAdj= data[1:]
		adjList.append([vertex, vertexAdj])
	input_file.close()
	return adjList

# if __name__ == '__main__':
# 	print (buildAdjList('kargerMinCut.txt'))

# def randomPickEdge(adjList):
# 	""" list -> (list of vertex, vertex)

# 	Return a two item tuple, which represent two vertex as a edge.
# 	"""
# 	adjListRandom = random.randint(0, len(adjList)-1)
# 	vertexAdjRandom = random.randint(0, len(adjList[adjListRandom][1])-1)
# 	vertexList = adjList[adjListRandom][0]
# 	newAdjVertex = adjList[adjListRandom][1][vertexAdjRandom]
# 	return (vertexList, newAdjVertex)

# if __name__ == '__main__':
# 	print (randomPickEdge(buildAdjList('kargerMinCut.txt')))

def kargerAlogrithm(adjList):
	""" adjList -> list

	adjList is a listof list; 
	list is two item list e.g. [[3, 4], [6, 7]]

	Return a list which has two list as item, which is the kargerMinCut
	"""
	# print adjList
	if len(adjList) <= 2:
		return adjList
	else:
		newAdjList = contract(adjList)
		return kargerAlogrithm(newAdjList)

def contract(adjList):
	newAdjList = copy.deepcopy(adjList)

	# randomly find a edge of the adjList
	adjListIndex = random.randint(0, len(newAdjList)-1)
	vertexAdjIndex = random.randint(0, len(newAdjList[adjListIndex][1])-1)
	newAdjVertex = newAdjList[adjListIndex][1][vertexAdjIndex] # which is a vertex
	vertexList = newAdjList[adjListIndex][0] # which is a list of vertex

	# find the index of newAdjVertex in the newAdjVertex
	newIndex = findIndexVertex(newAdjVertex, adjList)

	# put the newAdjVertex in the vertexList, which is the main contract
	newAdjList[adjListIndex][0].extend(newAdjList[newIndex][0])
	newAdjList[adjListIndex][1].extend(newAdjList[newIndex][1])

	# remove self loop, use alterList as a temp list.
	alterList = []
	for vertex in newAdjList[adjListIndex][1]:
		if vertex not in newAdjList[adjListIndex][0]:
			alterList.append(vertex)
	newAdjList[adjListIndex][1] = alterList

	# remove item of newIndex in newAdjList
	newAdjList.pop(newIndex)

	return newAdjList


def findIndexVertex(invdexVal, adjList):
	""" (invdexVal, adjList) -> int

		invdexVal -> int; adjList-> list 
		Return the index of the invdexVal in the first item of adjList
	
		>>> (3, [[[3, 4], [45, 234, 34]], ...])
		0
	"""
	for i in xrange(len(adjList)):
		if invdexVal in adjList[i][0]:
			return i


if __name__ == '__main__':
	adjList = buildAdjList('kargerMinCut.txt')
	# adjList = [[[1],[2,3,4]],[[2],[1,3,4]],[[3],[1,2,4]],[[4],[1,2,3]]]
	# print adjList
	minCutCount = []
	for i in xrange(100):
		resList = kargerAlogrithm(adjList)[0]
		count = len(resList[1])
		minCutCount.append(count)
	
	print min(minCutCount)


