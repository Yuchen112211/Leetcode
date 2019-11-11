'''

330. Patching Array
Hard

Given a sorted positive integer array nums and an integer n, add/patch elements to the array such that any number in range [1, n] inclusive can be formed by the sum of some elements in the array. Return the minimum number of patches required.

Example 1:

Input: nums = [1,3], n = 6
Output: 1 
Explanation:
Combinations of nums are [1], [3], [1,3], which form possible sums of: 1, 3, 4.
Now if we add/patch 2 to nums, the combinations are: [1], [2], [3], [1,3], [2,3], [1,2,3].
Possible sums are 1, 2, 3, 4, 5, 6, which now covers the range [1, 6].
So we only need 1 patch.

Example 2:

Input: nums = [1,5,10], n = 20
Output: 2
Explanation: The two patches can be [2, 4].

Example 3:

Input: nums = [1,2,2], n = 5
Output: 0

Solution:
Now we initialize the cur_upper to be 1, which means this is the number we'll cover the top.
Then we go through the provided nums.

For each number in nums, if the number is smaller than cur_upper, which means we can make
our top to be number + cur_upper, because every number before cur_upper is covered.

If the number is bigger than cur_upper, which means that there's an hole in the range, we need
to fill it, in order to fill this hole, we put cur_upper to be the added element for patches.
Since every number before cur_upper is covered, once we add this cur_upper to patch, we can have
the cur_upper double its value.

Once after we went through all the numbers in nums, we simply double the value of cur_upper, because 
afters we add curr_upper, we have the double range.

Then return the length of the add_nums.

The time complexity might as well as be O(log n).
'''
class Solution(object):
	def minPatches(self, nums, n):
		"""
		:type nums: List[int]
		:type n: int
		:rtype: int
		"""
		
		cur_upper = 1
		idx = 0
		add_nums = []
		while cur_upper <= n:
			
			if idx < len(nums):
				if nums[idx] <= cur_upper:
					cur_upper += nums[idx]
					idx += 1
				elif nums[idx] > cur_upper:
					add_nums.append(cur_upper)
					cur_upper += cur_upper
			else:
				cur_upper += cur_upper
				add_nums.append(cur_upper)
				
		return len(add_nums)


		
if __name__ == '__main__':
	s = Solution()
	nums = [1,2,31,33]
	n = 2147483647
	print s.minPatches(nums,n)