'''

498. Diagonal Traverse
Medium

Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Solution:
Get the diagonal sequence as the original sequences first, then reverse the even rows and form them all into one list.

Relatively simple.
'''
class Solution(object):
	def findDiagonalOrder(self, matrix):
		if not matrix:
			return []
		if not matrix[0]:
			return []
		M = len(matrix)
		N = len(matrix[0])
		if N == 1:
			rst = []
			for i in matrix:
				rst += i
			return rst
		#Do a traverse from the top left point to the bottom right point
		#And construct the original sequence.
		sequence = []
		for i in range(N):
			tmp = []
			currentNode = [0, i]
			while currentNode[1] >= 0 and currentNode[0] < M:
				tmp.append(matrix[currentNode[0]][currentNode[1]])
				currentNode[0] += 1
				currentNode[1] -= 1
			sequence.append(tmp)
		for i in range(1, M):
			tmp = []
			currentNode = [i, N - 1]
			while currentNode[0] < M and currentNode[1] >= 0:
				tmp.append(matrix[currentNode[0]][currentNode[1]])
				currentNode[0] += 1
				currentNode[1] -= 1
			sequence.append(tmp)
		rst = []
		for i in range(len(sequence)):
			if not i % 2:
				rst += sequence[i][::-1]
			else:
				rst += sequence[i]
		return rst

S = Solution()
matrix = [[2,5],[8,4],[0,-1]]

print S.findDiagonalOrder(matrix)