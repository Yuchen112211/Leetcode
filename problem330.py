class Solution(object):
	def minPatches(self, nums, n):
		"""
		:type nums: List[int]
		:type n: int
		:rtype: int
		"""
		
		cur_upper = 1
		idx = 0
		add_nums = []
		while cur_upper <= n:
			
			if idx < len(nums):
				if nums[idx] <= cur_upper:
					cur_upper += nums[idx]
					idx += 1
				elif nums[idx] > cur_upper:
					print cur_upper
					raw_input('Hold')
					add_nums.append(cur_upper)
					cur_upper += cur_upper
			else:
				cur_upper += cur_upper
				add_nums.append(cur_upper)
				print cur_upper
				raw_input('Hold')
				
		return len(add_nums)


		
if __name__ == '__main__':
	s = Solution()
	nums = [1,2,31,33]
	n = 2147483647
	print s.minPatches(nums,n)