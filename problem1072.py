'''

1072. Flip Columns For Maximum Number of Equal Rows
Medium

Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

Return the maximum number of rows that have all values equal after some number of flips.

 

Example 1:

Input: [[0,1],[1,1]]
Output: 1
Explanation: After flipping no values, 1 row has all values equal.

Example 2:

Input: [[0,1],[1,0]]
Output: 2
Explanation: After flipping values in the first column, both rows have equal values.

Example 3:

Input: [[0,0,0],[0,0,1],[1,1,0]]
Output: 2
Explanation: After flipping values in the first two columns, the last two rows have equal values.

Solution:

Every row can be transfered to start with 0.
If a row already starts with 0, great, maintain that, if it starts with 1, flip every elemtn
in this row.
Then we simply count the times that each form appears, then return the max apperance time.

'''

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