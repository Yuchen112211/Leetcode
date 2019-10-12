class Solution(object):
	def findMedianSortedArrays(self, nums1, nums2):
		index1 = len(nums1)/2
		index2 = len(nums2)/2
		is_odd_1 = len(nums1) % 2
		is_odd_2 = len(nums2) % 2
		while index1 > 0 and index1 < len(nums1) and index2 > 0 and index2 < len(nums2):
			smaller1 = nums1[:index1]
			bigger1 = nums1[index1:]
			smaller2 = nums2[:index2]
			bigger2 = nums2[index2:]
			if is_odd_1:
				bigger1 = bigger1[1:]
			if is_odd_2:
				bigger2 = bigger2[1:]
			if smaller1[-1] > bigger2[0]:
				index1 -= 1
				index2 += 1
			if smaller2[-1] > bigger1[0]:
				index1 += 1
				index2 -= 1

		print nums1[index1],nums2[index2]


if __name__  == '__main__':
	s = Solution()
	s.findMedianSortedArrays([1,2,3],[4,5,6,7,8])