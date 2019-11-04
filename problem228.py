class Solution(object):
	def summaryRanges(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[str]
		"""
		index1,index2 = 0,1
		rst = []
		while index2 < len(nums)+1:
			if index2 == len(nums):
				if index1 == index2-1:
					rst.append(str(nums[index1]))
				else:
					rst.append(str(nums[index1])+'->'+str(nums[index2-1]))
				index1 = index2
				index2 = index2 + 1
				break
			elif nums[index2] - nums[index2-1] == 1:
				index2 += 1
			else:
				if index1 == index2-1:
					rst.append(str(nums[index1]))
				else:
					rst.append(str(nums[index1])+'->'+str(nums[index2-1]))
				index1 = index2
				index2 = index2 + 1
		print index1,index2
		return rst

		
if __name__ == '__main__':
	s = Solution()
	nums = [0,2,3,4,6,8,9,11]
	print s.summaryRanges(nums)