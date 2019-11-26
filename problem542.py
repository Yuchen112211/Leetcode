'''
542. 01 Matrix
Medium

Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:

Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]

Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Solution:
BFS, but can be optimized.

'''
class Solution(object):
	def updateMatrix(self, matrix):
		if not matrix:
			return []
		def isValid(x,y):
			return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])

		from collections import deque
		rst = [[float('inf') for i in matrix[0] ] for k in matrix]
		stack = deque([])
		for i in range(len(matrix)):
			for k in range(len(matrix[0])):
				if matrix[i][k] == 0:
					stack.append((i,k))
					rst[i][k] = 0
		diffX = [1,-1,0,0]
		diffY = [0,0,1,-1]
		while stack:
			tmp = deque([])
			while stack:
				i,k = stack.pop()
				for d in range(4):
					if isValid(i+diffX[d], k+diffY[d]):
						if rst[i+diffX[d]][k+diffY[d]] == float('inf'):
							rst[i+diffX[d]][k+diffY[d]] = rst[i][k] + 1
							tmp.append((i+diffX[d], k+diffY[d]))
			stack = tmp
		return rst




s = Solution()
matrix = [[0,1,0],
 [0,1,0],
 [1,1,1]]
for i in s.updateMatrix(matrix):
	print i