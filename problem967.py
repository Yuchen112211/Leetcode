'''

967. Numbers With Same Consecutive Differences
Medium

Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K.

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one leading zero and is invalid, but 0 is valid.

You may return the answer in any order.

 

Example 1:

Input: N = 3, K = 7
Output: [181,292,707,818,929]
Explanation: Note that 070 is not a valid number, because it has leading zeroes.

Example 2:

Input: N = 2, K = 1
Output: [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]

Solution:
Use dp to solve this problem.
Compute each steps of numbers with K difference iteratively, use the numbers in the previous iteration to compute current list.

'''
class Solution(object):
	def numsSameConsecDiff(self, N, K):
		"""
		:type N: int
		:type K: int
		:rtype: List[int]
		"""
		dp = [[] for i in range(N)]
		if N == 1:
			return [i for i in range(10)]
		for i in range(1,10):
			dp[0].append(str(i))
		for digitNum in range(1, N):
			for previousNumber in dp[digitNum - 1]:
				lastNum = int(previousNumber[-1])
				if lastNum - K >= 0:
					dp[digitNum].append(previousNumber + str(lastNum - K))
				if lastNum + K < 10:
					dp[digitNum].append(previousNumber + str(lastNum + K))

		return list(set([int(i) for i in dp[-1]]))

s = Solution()
N = 3
K = 1
print s.numsSameConsecDiff(N, K)