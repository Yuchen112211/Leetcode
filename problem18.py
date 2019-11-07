'''

18. 4Sum
Medium

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]


Solution:
With every element, we do the three sum algorithm.

'''

class Solution:
	def fourSum(self, nums, target):
		res = []
		nums.sort()
		for i in range(len(nums)):
			if i == 0 or nums[i] > nums[i-1]:#Without the =, we can skip the duplicate.
				diff = target - nums[i]
				threeSums = self.threeSum(nums[i+1:], diff)
				for threeSum in threeSums:
					res.append([nums[i]] + threeSum)
		return res
				
		
	def threeSum(self, nums, target):
		res = []
		if len(nums) < 3: return res

		for i in range(len(nums) - 2):
			if i > 0 and nums[i] == nums[i-1]: continue
			l, r = i + 1, len(nums) - 1
			while l < r :
				s = nums[i] + nums[l] + nums[r]
				if s == target:
					res.append([nums[i] ,nums[l] ,nums[r]])
					l += 1; r -= 1
					while l < r and nums[l] == nums[l - 1]: l += 1
					while l < r and nums[r] == nums[r + 1]: r -= 1
				elif s < target :
					l += 1
				else:
					r -= 1
		return res 

if __name__ == '__main__':
	nums = [0,1,5,0,1,5,5,-4]
	s = Solution()
	print s.fourSum(nums,11)