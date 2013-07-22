remove items in a which are in b

a = [2, 3, 4, 1, 5, 7]
b = [1, 4]
# for vertex in a:
# 	# print vertex, a, b
# 	if vertex in b:
# 		a.remove(vertex)
# print a



# >>> result
# 2 [2, 3, 4, 1, 5, 7] [1, 4]
# 3 [2, 3, 4, 1, 5, 7] [1, 4]
# 4 [2, 3, 4, 1, 5, 7] [1, 4]
# 5 [2, 3, 1, 5, 7] [1, 4]
# 7 [2, 3, 1, 5, 7] [1, 4]
# [2, 3, 1, 5, 7]

# lesson from these code, never change the during iteration,
# it can produce some bugs which are very difficult to debug.

# the following code is not right either, it will promp out "list index out of range"
# notice that 'a' also has been changed in the loop which we use the item 'a[i]'
# n = len(a)
# for i in xrange(n):
# 	if a[i] in b:
# 		a.remove(a[i])
# print a


# the following is the right code, and everying is immutable
res = []
for item in a:
	if item not in b:
		res.append(item)
print res
