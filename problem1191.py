'''

1191. K-Concatenation Maximum Sum
Medium

Given an integer array arr and an integer k, modify the array by repeating it k times.

For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2, 1, 2, 1, 2].

Return the maximum sub-array sum in the modified array. Note that the length of the sub-array can be 0 and its sum in that case is 0.

As the answer can be very large, return the answer modulo 10^9 + 7.

 

Example 1:

Input: arr = [1,2], k = 3
Output: 9

Example 2:

Input: arr = [1,-2,1], k = 5
Output: 2

Example 3:

Input: arr = [-1,-2], k = 7
Output: 0

Solution:
In order to find the maximum subarray, there are several situations:
1. The original array has a negative sum.
2. The original array has a positive sum, but the sum is smaller than the maximum subarray when link two same arrays.
3. The original array has a positive sum, and the sum is bigger than the maximum subarray when link two same arrays.

Why can we find the maximum subarray when we link only two of the same arrays? In situation 1, we should not include one whole original array in our maximum subarray
in concatenated array, since the sum is negative, if we go through the whole array, there is no point. In situation 2, since the sum is smaller than the maximum subarray,
that means there are some middle elements in the original array are missed in the maximum subarray when we linked two of the same arrays. That means the maximum subarray
would include some part of the tail of first array and some part of the head of the second array.

So we can only use two array to find out the maximum subarray.
After this, we can now see the fun part.

The maximum subarray cross two subarray can only be selected once, but the whole original array can be selected k times.
Each maximum subarray would use 2 original arrays to form, so we can choose k-2 times the original array if the sum of it is positive.

Somehow we can guarantee that the maximum subarray is bigger than the sum of 2 linked arrays, since it is the maximum subarray we can find in the linked array.

Thus, in the end of the function, if the sum of original array is positive, return k-2 * sum + maximum array, if negative, return the maximum array.
'''
class Solution(object):
	def kConcatenationMaxSum(self, arr, k):
		"""
		:type arr: List[int]
		:type k: int
		:rtype: int
		"""
		def maxSubArray(nums):
			arr = [0] * len(nums)
			arr[0] = nums[0]
			for i in range(1,len(nums)):
				if arr[i-1] < 0:
					arr[i] = nums[i]
				else:
					arr[i] = arr[i-1] + nums[i]
			return max(arr)
		if k == 0:
			return 0

		sums = sum(arr)
		newArr = arr * 2
		rst = maxSubArray(newArr)

		if rst < 0:
			return 0

		if sums > 0:
			return (sums * (k-2) + rst) % (pow(10, 9) + 7)
		else:
			return rst % (pow(10, 9) + 7)
 
s = Solution()
arr = [-1,-2]
k = 2
print s.kConcatenationMaxSum(arr, k)

