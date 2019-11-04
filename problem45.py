class Solution(object):
	def jump(self, nums):
		if len(nums)==1:
			return 0
		elif max(nums)<=1:
			return len(nums)-1
		
		min_step = 0
		cur = len(nums)-1
		while True:
			for i in range(cur):
				if i + nums[i] >= cur:
					cur = i
					min_step += 1
					if cur == 0:
						return min_step
					break

if __name__ == '__main__':
	s = Solution()
	nums = [2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,6,3,5,2,2,6,3]

	print s.jump(nums)