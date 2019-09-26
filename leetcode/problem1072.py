class Solution(object):
	def maxEqualRowsAfterFlips(self, matrix):
		"""
		:type matrix: List[List[int]]
		:rtype: int
		"""
		if not matrix:
			return 0

		construct = {}
		for i in matrix:
			tmp = ''
			if i[0] == 0:
				for k in i:
					tmp += str(k)
			else:
				for k in i:
					tmp += str(1-k)
			if tmp in construct:
				construct[tmp] += 1
			else:
				construct[tmp] = 1
		return max(construct.values())
		
if __name__ == '__main__':
	s = Solution()
	matrix = [[0,0,0],[0,0,1],[1,1,0]]
	print s.maxEqualRowsAfterFlips(matrix)