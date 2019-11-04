class Solution(object):
	def findUnsortedSubarray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		from bisect import bisect_left
		rst = []
		status = [False for i in nums]
		for i in range(len(nums)):
			
s = Solution()
nums = [2,6,4,8,10,9,15]
s.findUnsortedSubarray(nums)