'''

503. Next Greater Element II
Medium

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:

Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.

Solution:
I thought I could use min heap, but the nextGreaterElements should find the greater element circularly. Which means that if not found the next
greater element until the tail of the array, we need to move to the index to the head of the array.

So min heap is dead.

The solution on Leetcode says using stack is acceptable, instead of go over the numbers only once,
the iteration would happen on length 2*length-1, which means that if there's a bigger element, one would
definitely find that.

Actually this solution does exactly the same as I did below, only extended the length of iteration.

I first used heapq, however the heapify operation is not neccessary, use the deque would perfectly solve the problem.

Remember, the trick to solve this problem, is go through the numbers double time.
'''
class Solution(object):
	def nextGreaterElements(self, nums):
		import collections
		if not nums:
			return []
		stack = collections.deque([nums[-1]])
		maxElement = max(nums)
		arr = [-1] * len(nums)
		length = len(nums)
		for i in range(2*length-1, -1, -1):
			while stack:
				if stack[-1] <= nums[i % length]:
					stack.pop()
				else:
					break
			if not stack:
				arr[i % length] = -1
			else:
				arr[i % length] = stack[-1]
			stack.append(nums[i % length])
		return arr

if __name__ == '__main__':
	s = Solution()
	nums = [1,2,3,4,3]
	print s.nextGreaterElements(nums)