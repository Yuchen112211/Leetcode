'''

416. Partition Equal Subset Sum
Medium

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

    Each of the array element will not exceed 100.
    The array size will not exceed 200.

 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].

 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets

Solution:
DP solution.
Define if the every number before the half, and then determine the num can be formated by the selection
of the nums list.

What we really need is the last element of the dp list.

Double for loop, update the all dp list on the given current num. Just use the dp[i] and dp[i-num]
on a OR operation. The bottom edge is the current num, in the list iteration operation, when the
second parameter is n, it would stop at n+1.

All the way from the half, to the current number's boarder.

'''


class Solution(object):
	def canPartition(self, nums):
		all_sums = sum(nums)
		if all_sums % 2 == 1:
			return False
		half = all_sums / 2

		dp = [False] * (half + 1)
		dp[0] = True

		for num in nums:
			for i in range(half, num-1, -1):
				dp[i] = dp[i] or dp[i-num]

		return dp[-1]