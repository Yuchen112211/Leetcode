'''

200. Number of Islands
Medium

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1

Example 2:

Input:
11000
11000
00100
00011

Output: 3

Solution:
Use a BFS, starting with any cell that contains a 1. Set its neightbors to be 0
and push them into the stack. In the for loop, everytime we encounter a 1, we plus
1 to count.

The count outside the loop means the number of the unions.

'''


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