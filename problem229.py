'''
229. Majority Element II
Medium

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]

Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]

Solution:

First find the two numbers that appears the most frequently.

For the first iteration, it's complicated to to explain but easy to understand by reading the code.
This would guarantee at the end of the iteration, the two numbers are the most frequent numbers in
the un-sorted array.

Then simply compare these two numbers to the 1/3 * len(nums)

'''
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1,num2 = 0,0
        cnt1,cnt2 = 0,0
        index = 0
        while index < len(nums):
        	if nums[index] == num1:
        		cnt1 += 1
        	elif nums[index] == num2:
        		cnt2 += 1
        	elif cnt1 == 0:
        		num1 = nums[index]
        		cnt1 = 1
        	elif cnt2 == 0:
        		num2 = nums[index]
        		cnt2 = 1
        	else:
        		cnt1 -= 1
        		cnt2 -= 1
        	index += 1
        cnt1,cnt2 = 0,0
        index = 0
        while index < len(nums):
        	if nums[index] == num1:
        		cnt1 += 1
        	if nums[index] == num2:
        		cnt2 += 1
        	index += 1
        rst = set()
        if cnt1 > len(nums)/3.0:
        	rst.add(num1)
        if cnt2 > len(nums)/3.0:
        	rst.add(num2)
        return list(rst)


if __name__ == '__main__':
	S = Solution()
	print S.majorityElement([3,2,3])