'''

286. Walls and Gates
Medium

You are given a m x n 2D grid initialized with these three possible values.

    -1 - A wall or an obstacle.
    0 - A gate.
    INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF

After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4

Solution:
Simple BFS problem, only remember to check if the neightbor can be update to a smaller value, if so, update the value and
add the neightbor to the next round of BFS, since we need to update everything.

Again, simple bfs.

'''
class Solution(object):
	def wallsAndGates(self, rooms):
		if not rooms:
			return
		if not rooms[0]:
			return 
		M = len(rooms)
		N = len(rooms[0])
		x = [0,0,1,-1]
		y = [1,-1,0,0]

		def bfs(node):
			currentValue = rooms[node[0]][node[1]]
			stack = [node]
			while stack:
				tmp = []
				while stack:
					currentNode = stack.pop()
					for i in range(4):
						nx = x[i] + currentNode[0]
						ny = y[i] + currentNode[1]
						if 0 <= nx < M and 0 <= ny < N:
							if rooms[nx][ny] > rooms[currentNode[0]][currentNode[1]] + 1:
								rooms[nx][ny] = rooms[currentNode[0]][currentNode[1]] + 1
								tmp.append((nx,ny))
				stack = tmp


		for i in range(M):
			for k in range(N):
				if rooms[i][k] == 0:
					bfs((i,k))



inf = float('inf')
rooms = [ [inf, -1, 0, inf],
[inf, inf, inf , -1],
[inf, -1, inf, -1],
[0, -1, inf, inf]]
S = Solution()
S.wallsAndGates(rooms)
for i in rooms:
	print i