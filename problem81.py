'''

81. Search in Rotated Sorted Array II
Medium

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:

Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:

Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Solution:
Use step of 1 or -1 to find out whether to increase or decrease the index.
Start from 0.
Iteration would solve this problem. O(n) solution.
Could use binary binomial search, should be O(log n). But the problem is when doing binary search,
once the middle has other same numbers, it would get crazy.

'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        index,move = 0,0
        if target == nums[0]:
            return True
        
        if target < nums[0]:
            index = -1
            move = -1
        if target > nums[0]:
            index = 0
            move = 1
        while abs(index) < len(nums):
            if nums[index] == target:
                return True
            index += move

        return False

if __name__ == '__main__':
    x = Solution()
    print x.search([2,5,6,0,0,1,2],3)