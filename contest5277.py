
class Solution(object):
	def countSquares(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""
		rst = 0
		for i in range(len(matrix)):
			for k in range(len(matrix[0])):
				if i >= 1 and k >= 1 and matrix[i][k] == 1:
					matrix[i][k] = max(min(matrix[i-1][k], matrix[i][k-1],matrix[i-1][k-1]) + 1, matrix[i][k])
		
		for i in matrix:
			rst += sum(i)
		return rst

s = Solution()

matrix =[[0,0,0],[0,1,0],[0,1,0],[1,1,1],[1,1,0]]
print s.countSquares(matrix)