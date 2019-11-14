'''

494. Target Sum
Medium

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.

Note:

	The length of the given array is positive and will not exceed 20.
	The sum of elements in the given array will not exceed 1000.
	Your output answer is guaranteed to be fitted in a 32-bit integer.

Solution:
DP solution is super slow, I do know why, maybe we can use a dictionary?

'''

'''
Recursive:TLE
class Solution(object):
	ans = 0
	def findTargetSumWays(self, nums, S):
		def trav(i, current, target):
			if i == len(nums):
				if current == target:
					self.ans += 1
				return

			trav(i+1, current + nums[i], target)
			trav(i+1, current - nums[i], target)
		
		trav(0, 0, S)
		return self.ans
'''

'''
DP:Super Slow
class Solution(object):
	def findTargetSumWays(self, nums, S):
		if S > 1000 or S < -1000:
			return 0
		length = len(nums)
		allSum = sum(nums)
		if allSum < S or -allSum > S:
			return 0
		dp = [ [0 for i in range(allSum * 2 + 1)] for k in nums]
		dp[0][nums[0] + allSum] = 1
		dp[0][-nums[0] + allSum] += 1
		for i in range(1, len(nums)):
			for k in range(len(dp[i])):
				if k >= nums[i]:
					dp[i][k] = dp[i-1][k-nums[i]]
				if k < allSum * 2 + 1 - nums[i]:
					dp[i][k] += dp[i-1][k+nums[i]]
		return dp[len(nums)-1][S + allSum]
'''

class Solution(object):
	def findTargetSumWays(self, nums, S):
		import collections

		recorded = collections.defaultdict(int)
		recorded[(0,nums[0])] = 1
		recorded[(0,-nums[0])] = 1
		for i in range(1,len(nums)):
			for k in recorded:




if __name__ == '__main__':
	s = Solution()
	nums = [1, 1, 1, 1, 1]
	S = 3
	print s.findTargetSumWays(nums, S)