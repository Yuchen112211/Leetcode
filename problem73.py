'''

73. Set Matrix Zeroes
Medium

Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:

Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Solution:
Record every 0's index, update the whole column and row of the index.

Remember to record the original indexes, not a bfs, since the 0 added to the matrix is not candidates for the modify.

'''

class Solution(object):
	def setZeroes(self, matrix):
		def modify(matrix,index):
			for i in range(len(matrix)):
				matrix[i][index[1]] = 0
			for i in range(len(matrix[0])):
				matrix[index[0]][i] = 0

		to_modify = []
		for i in range(len(matrix)):
			for k in range(len(matrix[0])):
				if matrix[i][k] == 0:
					to_modify.append((i,k))
		for i in to_modify:
			modify(matrix,i)
		
if __name__ == '__main__':
	s = Solution()
	matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
	s.setZeroes(matrix)