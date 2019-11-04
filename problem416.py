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