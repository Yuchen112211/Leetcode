'''

15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Solution:

First solution uses two pointers.
After we sort the array, for each element between 0 and len(nums)-3, we find the whether the
next 2 elements in the later sequence using two pointers.
The l pointer starts at i+1, the r pointer starts at the tail. If the i+r+l (element sum) 
is bigger than the target, we would minus the r by 1, since the list is sorted. If the
sum is smaller than the target, add 1 to l. If equals, we simply append the sequence into
out result.

In sum equals the target situation, we need to relocate the l and r pointers so that no
duplicated elements are included.

Since the list is already sorted, we do not need to worry about the duplication after we
move both pointers.


However, another possible way is to divide all numbers into positive, zeroes and negatives.
This solution, umm, TLE. Wonder why. Maybe is the if in list operation costs too much time.

'''


class Solution:
	def threeSum(self, nums):
		target = 0
		res = []
		nums.sort()
		if len(nums) < 3: return res

		for i in range(len(nums) - 2):
			if i > 0 and nums[i] == nums[i-1]: continue
			l, r = i + 1, len(nums) - 1
			while l < r :
				s = nums[i] + nums[l] + nums[r]
				if s == target:
					res.append([nums[i] ,nums[l] ,nums[r]])
					l += 1; r -= 1
					while l < r and nums[l] == nums[l - 1]: l += 1
					while l < r and nums[r] == nums[r + 1]: r -= 1
				elif s < target :
					l += 1
				else:
					r -= 1
		return res 
'''

class Solution:
	def threeSum(self, nums):
		from itertools import combinations
		target = 0
		res = []
		nums.sort()
		if len(nums) < 3: return res

		pos = []
		neg = []
		zero = 0
		for i in nums:
			if i > 0:
				pos.append(i)
			elif i < 0:
				neg.append(i)
			else:
				zero += 1
		
		set_pos = set(pos)
		set_neg = set(neg)
		if zero >= 3:
			res.append([0,0,0])

		if zero >= 1:
			for i in set_pos:
				if -i in set_neg:
					res.append([-i,0,i])

		if len(pos) > 1 and len(neg) > 0:
			for i in combinations(pos,2):
				sum_now = i[0] + i[1]
				if -sum_now in set_neg:
					current_l = [-sum_now,i[0],i[1]]
					if current_l not in res:
						res.append(current_l)
						
		if len(neg) > 1 and len(pos) > 0:
			for i in combinations(neg,2):
				sum_now = i[0] + i[1]
				if -sum_now in set_pos:
					current_l = [i[0],i[1],-sum_now]
					if current_l not in res:
						res.append(current_l)
		return res
'''

if __name__ == '__main__':
	nums = [-1,0,1,2,-1,-4]

	s = Solution()
	print s.threeSum(nums)