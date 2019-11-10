'''
228. Summary Ranges
Medium

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


Solution:
One pass iteration, once encounter a number that is not in ascending order, simply get the range into
rst, finally form as the structure that the question is requiring.

'''

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