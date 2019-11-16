'''

698. Partition to K Equal Sum Subsets
Medium

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Solution:
Use greedy and backtrack. Maybe not so greedy. maintain k groups, add each element into 
the current group until the group can not take any more. group + v condition would fit all kinds of 
situations.

So sort the array first, if the biggest one is bigger than part sum, then we can not part the array.
After the sort, this is a greedy procedure.
Then there is a classic backtrack.

If some number is the same as the target, we simply pop it out and minus k by 1.

'''
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        target, rem = divmod(sum(nums), k)
        if rem: return False

        def search(groups):
            if not nums: return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups): return True
                    groups[i] -= v
                if not group: break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)

if __name__ == '__main__':
	s = Solution()
	nums = [4, 3, 2, 3, 5, 2, 1]
	k = 3
	print s.canPartitionKSubsets(nums,k)