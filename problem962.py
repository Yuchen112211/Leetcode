'''

962. Maximum Width Ramp
Medium

Given an array A of integers, a ramp is a tuple (i, j) for which i < j and A[i] <= A[j].  The width of such a ramp is j - i.

Find the maximum width of a ramp in A.  If one doesn't exist, return 0.

 

Example 1:

Input: [6,0,8,2,1,5]
Output: 4
Explanation: 
The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.

Example 2:

Input: [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: 
The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.

 

Note:

    2 <= A.length <= 50000
    0 <= A[i] <= 50000

Solution:
Sort the array by the elements' value, but store the indexes.

During the iteration, keep record of the least index, since the array is increasing as the index gets bigger(original order), everything before is smaller than
after, so for each iteration time we update the answer to be current index minus the smallest index, and update the smallest index.

'''
class Solution(object):
    def maxWidthRamp(self, A):
        ans = 0
        m = float('inf')
        for i in sorted(range(len(A)), key = A.__getitem__):
            ans = max(ans, i - m)
            m = min(m, i)
        return ans
s = Solution()
print s.maxWidthRamp([9,8,1,0,1,9,4,0,4,1])