'''

861. Score After Flipping Matrix
Medium

We have a two dimensional matrix A where each value is 0 or 1.

A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.

After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.

Return the highest possible score.

 

Example 1:

Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Solution:
There are only two kinds of move, flip the whole column or whole row.

For the row flip, we change each digit in the same row, however we flip this row, the bigger number would be 1 being the first digit.
Since the digits are only consist of 0 and 1, once we flip the whole row, we flip the first digit, and with the bigger first digit, we 
can always find the bigger number with the exact same one.

For the column flip, we change every number on the same digit. For this flip, we could decide which can bring us the bigger score, flip the
column or stays the same. We do not consider the original numbers since the digits have same base, to decide flip or not, we can simply
count how many 1s would there be after the operations.
To simplify the decision, we can count the numbers of 1s and 0s for each column, and add the bigger number * base to the score.

To solve the problem, first iterate through the A list, determine whether the number should be flipped. Then go over every column, to find
the bigger number of 1s and 0s.

'''

class Solution(object):
	def matrixScore(self, A):
		"""
		:type A: List[List[int]]
		:rtype: int
		"""
		if not A:
			return 0

		for i in A:
			if i[0] == 0:
				for k in range(len(i)):
					i[k] = 1-i[k]
		score = 0
		for i in range(len(A[0])):
			cntZero = 0
			cntOne = 0
			for k in range(len(A)):
				if A[k][i] == 1:
					cntOne += 1
				else:
					cntZero += 1
			currentBase = pow(2, len(A[0]) - 1 - i)
			score += (currentBase * max(cntZero, cntOne))
		return score

		
A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
s = Solution()
print s.matrixScore(A)