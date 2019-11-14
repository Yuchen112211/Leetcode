'''

45. Jump Game II
Hard

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Solution:
In the following code, the cur index is the index that we can achieve with the min_step count.
Each iteration we start from the first, compute every i + nums[i], if i + nums[i] is bigger
than the cur index, which means with this step at the index i would reach the end of the path.

Every recursion after we found out the i, reset the cur to be i, start the next recursion.

Since the recursion starts from 0, which is the first element of the path, then as we encounter
the first element/cell that we can reach the tail, we can call it an optimized solution.

Actually this is a greedy approach, cannot start from the end, otherwise it can not be an optimized 
approach, the steps number is not minimum.

'''

class Solution(object):
	def jump(self, nums):
		if len(nums)==1:
			return 0
		elif max(nums)<=1:
			return len(nums)-1
		
		min_step = 0
		cur = len(nums)-1
		while True:
			for i in range(cur):
				if i + nums[i] >= cur:
					cur = i
					min_step += 1
					if cur == 0:
						return min_step
					break

if __name__ == '__main__':
	s = Solution()
	nums = [2,9,6,5,7,0,7,2,7,9,3,2,2,5,7,8,1,6,6,6,3,5,2,2,6,3]

	print s.jump(nums)