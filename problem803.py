class Solution(object):
	def hitBricks(self, grid, hits):
		"""
		:type grid: List[List[int]]
		:type hits: List[List[int]]
		:rtype: List[int]
		"""
		anotherGrid = [[i for i in k] for k in grid]
		for i,k in hits:
			anotherGrid[i][k] = 0

		connected = [[0 for i in k] for k in grid]
		for i in range(len(connected[0])):
			connected[0][i] = anotherGrid[0][i]
		hits = hits[::-1]
		for i,k in hits:
			pass
#To be continued

s = Solution()
grid = [[1,1,0,0],[1,1,1,1],[1,1,1,1]]
hits = [[1,1],[1,0]]
print s.hitBricks(grid, hits)