'''

581. Shortest Unsorted Continuous Subarray
Easy

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:

Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Solution:
Sort the array first, then compare the elements one by one.

'''
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rst = sorted(nums)
        cnt = []
        for i in range(len(nums)):
            if nums[i] != rst[i]:
                if len(cnt) <= 1:
                    cnt.append(i)
                else:
                    cnt[-1] = i
        if len(cnt) <= 1:
            return 0
        return cnt[1] - cnt[0] + 1

s = Solution()
nums = [2,6,4,8,10,9,15]
s.findUnsortedSubarray(nums)