'''

42. Trapping Rain Water
Hard

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Solution:
We maintain two max value and two pointers on left and right side. Use the iteration on this one.
Not DP solution, simple two pointers.

If the current left is less than current right value, which means that the left value should be 
processed, because we have to determine which is the lower boarder of the that we need to compute
the current trapped water.

If the left is lower, update the left_max if needed, if the left_max is updated, don't compute the
ans(don't add.), if not, which means the current height is lower than the left_max, then there would
be some trapped water, add the amount to the global variable.

Very intuitive, should review this in the future.

'''

class Solution(object):	
	ans = 0

	def trap(self,height):
		if not height:
			return 0
		left, right = 0, len(height) - 1
		left_max, right_max = height[left], height[right]

		while left < right:
			if height[left] < height[right]:
				if left_max <= height[left]:
					left_max = height[left]
				else:
					self.ans += (left_max - height[left])
				left += 1
			else:
				if right_max <= height[right]:
					right_max = height[right]
				else:
					self.ans += (right_max - height[right])
				right -= 1
		return self.ans


if __name__ == '__main__':
	height = [0,1,0,2,1,0,1,3,2,1,2,1]
	#[0,1,0,2,1,0,1,3,2,1,2,1]
	index = 2
	s = Solution()

	print s.trap(height)