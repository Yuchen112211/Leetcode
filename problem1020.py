'''

1020. Number of Enclaves
Medium

Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square, or off the boundary of the grid.

Return the number of land squares in the grid for which we cannot walk off the boundary of the grid in any number of moves.

 

Example 1:

Input: [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: 
There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.

Example 2:

Input: [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: 
All 1s are either on the boundary or can reach the boundary.


Solution:
Firstly we find out every 0 cell which are on the boarders, push them back into a stack.
Go over the stack, which is a pop operation, set the current position's 1 to 0
if its neighbors are 1, push them into the stack and go over as long as the stack is 
not empty.

Simple BFS.

Then we can initial a number, go over the grid and sum all cells, return the sum.
'''



class Solution(object):
	def numEnclaves(self, A):
		"""
		:type A: List[List[int]]
		:rtype: int
		"""
		def isValid(x,y):
			return 0 <= x < len(A) and 0 <= y < len(A[0])

		stack = []
		for i in range(len(A)):
			for k in range(len(A[0])):
				if i == 0 or i == len(A)-1 or k == 0 or k == len(A[0])-1:
					if A[i][k] == 1:
						stack.append((i,k))
		diff_x = [0,0,1,-1]
		diff_y = [1,-1,0,0]

		while stack:
			i,k = stack.pop()
			A[i][k] = 0
			for j in range(4):
				if isValid(i+diff_x[j],k+diff_y[j]):
					if A[i+diff_x[j]][k+diff_y[j]] == 1:
						stack.append((i+diff_x[j],k+diff_y[j]))

		rst = 0
		for i in A:
			rst += i
		return rst
		
if __name__ == '__main__':
	s = Solution()
	A = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
	print s.numEnclaves(A)