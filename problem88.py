class Solution(object):
	def merge(self, nums1, m, nums2, n):
		"""
		:type nums1: List[int]
		:type m: int
		:type nums2: List[int]
		:type n: int
		:rtype: None Do not return anything, modify nums1 in-place instead.
		"""
		index1,index2 = 0,m
		nums1[m:] = nums2
		print nums1[index1],nums1[index2]
		print nums1
		
if __name__ == '__main__':
	s = Solution()
	nums1 = [1,2,3,0,0,0]
	nums2 = [2,5,6]
	s.merge(nums1,3,nums2,3)