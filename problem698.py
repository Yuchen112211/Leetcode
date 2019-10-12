class Solution(object):
	def canPartitionKSubsets(self, nums, k):
		if k == 1:
			return True
		elif not nums:
			return False
		nums = sorted(nums)
		sum_all = sum(nums)
		partition = sum(nums) / float(k)
		if partition % 1 != 0:
			return False
		while nums:
			current_num = nums[-1]
			nums = nums[:-1]
			index = 0
			while current_num < partition:
				current_num += nums[index]
				index += 1
			if current_num != partition:
				return False
			nums = nums[index:]
		return True

if __name__ == '__main__':
	s = Solution()
	nums = [4, 3, 2, 3, 5, 2, 1]
	k = 3
	print s.canPartitionKSubsets(nums,k)