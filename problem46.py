'''

46. Permutations
Medium

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Solution:
Classic backtrack.

'''

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = []
        def backtrack(arr):
            if len(arr) == len(nums):
                rst.append(arr)
                return
            for i in nums:
                if i in arr:
                    continue
                else:
                    tmp = arr + [i]
                    backtrack(arr + [i])
        backtrack([])
        return rst

A = [1,2,3]
s = Solution()
print s.permute(A)