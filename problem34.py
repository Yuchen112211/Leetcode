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

class Solution(object):        
    def searchRange(self,nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch(arr, num):
            left = 0
            right = len(arr) - 1
            while left < right:
                if right - left == 1:
                    if arr[left] != num and arr[right] != num:
                        return -1
                    if arr[right] == num:
                        return right
                    if arr[left] == num:
                        return left
                mid = (left + right) / 2
                if arr[mid] == num:
                    return mid
                elif arr[mid] < num:
                    left = mid
                elif arr[mid] > num:
                    right = mid
            return -1
        if not nums:
            return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target:
                return [0,0]
            else:
                return [-1,-1]
            
        mid = binarySearch(nums, target)
        if mid == -1:
            return [-1, -1]
        left = mid
        right = mid
        while left >= 0:
            if nums[left] == target:
                left -= 1
            else:
                break
        while right < len(nums):
            if nums[right] == target:
                right += 1
            else:
                break
        return [left+1, right - 1]

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

print s.searchRange([5,7,7,8,8,10], 10)
