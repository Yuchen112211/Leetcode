'''

334. Increasing Triplet Subsequence
Medium

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.

Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true

Example 2:

Input: [5,4,3,2,1]
Output: false

Solution:
Maintain two min value, when there's a number that is bigger than the two maintained min
value, simply return True.
At the end of iteration, return False since there is no pair.

'''

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1 = min2 = max(nums)
        for i in nums:
            min1 = min(min1,i)
            if i > min1:
                min2 = min(min2,i)
            if i > min2:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    nums = [3,2,1]
    print s.increasingTriplet(nums)