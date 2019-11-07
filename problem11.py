'''

11. Container With Most Water
Medium

Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

 

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

 
Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

Solution:
Brute force would TLE.

scores = (r - l) * min(s[r],s[l])

Use two pointers here. Start from head and tail, compute the scores with each set of 
pointers. If the left pointer's height is lower, increase the left pointer, else, decrease
the right pointer, which would always make the height of the socres bigger or not smaller.

In this case, the complexity is O(n), where the Brute force is O(n^2)
'''

class Solution(object):
    def maxArea(self, height):
        start = 0
        end = len(height) - 1
        max_area = 0

        while start < end:

            width = end - start
            length = min(height[start], height[end])

            area = width * length

            if area > max_area:
                max_area = area

            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return max_area
