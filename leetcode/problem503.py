class Solution(object):
	def nextGreaterElements(self, nums):
		max_num = max(nums)
		rst = []
		index1 = index2 = 0
		length_num = len(nums)
		while index < length_num:
			if index == 0:
				rst.append(max(nums[1:]))
				continue
			if nums[index] > rst[-1]
if __name__ == '__main__':
