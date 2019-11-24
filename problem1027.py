'''

1027. Longest Arithmetic Sequence
Medium

Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

 

Example 1:

Input: [3,6,9,12]
Output: 4
Explanation: 
The whole array is an arithmetic sequence with steps of length = 3.

Example 2:

Input: [9,4,7,2,10]
Output: 3
Explanation: 
The longest arithmetic subsequence is [4,7,10].

Example 3:

Input: [20,1,15,3,10,5,8]
Output: 4
Explanation: 
The longest arithmetic subsequence is [20,15,10,5].

Solution:
Instead of the traditional dp list, use dp dictionary(hashmap).
Very interesting. 

For each index, go over every element before the index, substract the value, if the same value pair up with the iterated index is in the dictionary,
we add  the substracted value pair up with the current index into the dictionary.


class Solution(object):
	def longestArithSeqLength(self, A):
		"""
		:type A: List[int]
		:rtype: int
		"""
		dp = {}
		for i, a2 in enumerate(A[1:], start=1):
			for j, a1 in enumerate(A[:i]):
				d = a2 - a1
				if (j, d) in dp:
					dp[i, d] = dp[j, d] + 1
				else:
					dp[i, d] = 2
		return max(dp.values())

Actually this can be implemented by list, only store tuple?
2-D matrix?
This might be solvable by 2-D matrix, but the difference between the elements might be negative, so we need to double the length of dp list.
Might use too much memory.

Solved, memory would not explode, but the time is extremely long.
'''

class Solution(object):
	def longestArithSeqLength(self, A):
		maxLength = 0
		length = max(A) - min(A)
		dp = [[1 for i in range(length * 2 + 1)] for k in range(len(A))]
		for i in range(1, len(A)):
			for k in range(i):
				diff = A[i] - A[k] + length
				dp[i][diff] = dp[k][diff] + 1
		for i in dp:
			maxLength = max(maxLength, max(i))
		return maxLength

s = Solution()
A = [3,6,9,12]


ans = s.longestArithSeqLength(A)
print ans
