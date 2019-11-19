'''

88. Merge Sorted Array
Easy

Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

    The number of elements initialized in nums1 and nums2 are m and n respectively.
    You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

Solution:
Simply set the remaining elements in nums1 to be nums2. Then sort it. Then assign each of the element into nums1.

'''
class Solution(object):
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: None Do not return anything, modify nums1 in-place instead.
		"""
		nums1[m:] = nums2
		tmp = sorted(nums1)
		for i in range(len(tmp)):
			nums1[i] = tmp[i]
		
if __name__ == '__main__':
	s = Solution()
	nums1 = [1,2,3,0,0,0]
	nums2 = [2,5,6]
	s.merge(nums1,3,nums2,3)