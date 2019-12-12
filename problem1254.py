'''

Simple bfs problem.

'''

class Solution(object):
	def closedIsland(self, grid):
		M = len(grid)
		N = len(grid[0])

		boarderLand = set([])
		for i in range(M):
			if grid[i][0] == 0:
				boarderLand.add((i,0))
			if grid[i][N-1] == 0:
				boarderLand.add((i,N-1))
		for i in range(N):
			if grid[0][i] == 0:
				boarderLand.add((0,i))
			if grid[M-1][i] == 0:
				boarderLand.add((M-1, i))

		def bfs(node):
			x = [0,0,1,-1]
			y = [1,-1,0,0]
			stack = [node]
			while stack:
				tmp = []
				while stack:
					nextNode = stack.pop()
					grid[nextNode[0]][nextNode[1]] = 1
					for j in range(4):
						nx = x[j] + nextNode[0]
						ny = y[j] + nextNode[1]
						if 0 <= nx < M and 0 <= ny < N:
							if grid[nx][ny] == 0:
								tmp.append((nx,ny))
				stack = tmp

		for node in boarderLand:
			if grid[node[0]][node[1]] == 1:
				continue
			bfs(node)
		cnt = 0
		for i in range(M):
			for k in range(N):
				if grid[i][k] == 0:
					cnt += 1
					bfs((i,k))
		return cnt


S = Solution()
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
print S.closedIsland(grid)