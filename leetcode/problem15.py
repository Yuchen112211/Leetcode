class Solution(object):
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		from itertools import combinations
		nums = sorted(nums)

		def find2Sum(nums,target):
			head = 0
			tail = len(nums)-1
			rst = []
			while head != tail:
				sum_now = nums[head] + nums[tail]
				if nums[head] > target:
					break
					
				if sum_now == target:
					if [nums[head],nums[tail]] not in rst:
						rst.append([nums[head],nums[tail]])
					head += 1
				elif sum_now < target:
					head += 1
				elif sum_now > target:
					tail -= 1
			return rst

		rst = []
		index = 0
		while index < len(nums)-2:
			first_ele = nums[index]
			if first_ele > 0:
				 break
			target = -first_ele
			sum2 = find2Sum(nums[index+1:],target)
			tmp = []
			if sum2 != []:
				tmp = [[first_ele] + i for i in sum2]
				for i in tmp:
					if i not in rst:
						rst.append(i)
			index += 1
		return rst
		
if __name__ == '__main__':
	nums = [-1,0,1,2,-1,-4]

	s = Solution()
	print s.threeSum(nums)