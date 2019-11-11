'''
300. Longest Increasing Subsequence
Medium

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

Solution:

Use dp.

Initialize every element to be 1 in dp list, when iterate through the nums list, we have to iterate
through every node before the current num, and set the dp list current index to be the max dp value 
of previous elements.

This is not so elegent, but is O(n^2) complexity.
[a if b else c for i in x] means if each element satisfies c, the value should be a, else is c.

'''

            
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        arr = [1] * len(nums)
        for i in range(1,len(nums)):
            arr[i] = max([arr[i]+arr[k] if nums[i] > nums[k] else 1 for k in range(i)])
        return max(arr)

if __name__ == '__main__':
	nums = [10,9,2,5,3,7,101,18]
	S = Solution()
	print S.lengthOfLIS(nums)