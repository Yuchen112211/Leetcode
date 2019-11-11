'''
34. Find First and Last Position of Element in Sorted Array
Medium

Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Solution:
A relatively easy one, but will be difficult if not knowing what it's really asking.
This problem is actually a binary seach question, since we are finding the target's start and end
position, can be transformed to be two binary seach.

Using module bisect would make the process much easier for it has already implemented the two
methods.

'''

class Solution(Object):
    def searchRange(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1,-1]
        elif len(nums) == 1:
            if target == nums[0]:
                return [0,0]
            else:
                return [-1,-1]
        
        left = 0
        right = len(nums) - 1
        signal = 0
        while nums[(left+right)/2] != target:
            if right - left <= 1:
                if nums[right] == target:
                    left = right
                    break
                else:
                    signal = 1
                    break
            if nums[(left+right)/2] > target:
                right = (left+right)/2
            else:
                left = (left+right)/2
        if signal == 1:
            return [-1,-1]
        mid_index = (left+right) / 2
        left,right = mid_index,mid_index
        while nums[left] == target and left > 0:
            left -= 1
        while nums[right] == target and right < len(nums) - 1:
            right += 1
        left += 1
        right -= 1
        if nums[0] == target:
            left = 0
        if nums[-1] == target:
            right = len(nums) - 1
        return [left,right]

'''
class Solution(object):        
    def searchRange(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        import bisect
        index_1 = bisect.bisect_left(nums, target)
        index_2 = bisect.bisect_right(nums, target)
        if index_1 == index_2:
            return [-1,-1]
        return [index_1, index_2-1]
        

'''

s = Solution()

print s.searchRange([5,7,7,8,8,10])
