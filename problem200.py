class Solution(object):
	def numIslands(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		stack = []
		cnt = 0
		for ii in range(len(grid)):
			for kk in range(len(grid[0])):
				if grid[ii][kk] == "1":
					stack = [(ii,kk)]
					while stack:
						(i,k) = stack.pop()
						grid[i][k] = "0"
						if i - 1 >= 0 and grid[i-1][k] == "1":
							stack.append((i-1,k))

						if i + 1 < len(grid) and grid[i+1][k] == "1":
							stack.append((i+1,k))
						if k - 1 >= 0 and grid[i][k-1] == "1":
							stack.append((i,k-1))
						if k + 1 < len(grid[0]) and grid[i][k+1] == "1":
							stack.append((i,k+1))
					cnt += 1
		return cnt



if __name__ == "__main__":
	grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
	s = Solution()
	print s.numIslands(grid)