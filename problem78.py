'''

78. Subsets
Medium

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

Solution:
Maintain a list of list, for every element, add the element to each of the list, then add this new
list to the list of list.
Maybe the explanation is confusing, but the code is actually simple.

'''
class Solution(object):

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rst = [[]]

        for num in nums:
        	length_rst = len(rst)
        	for i in range(length_rst):
        		next_set_element = rst[i] + [num]
        		rst.append(next_set_element)
        return rst



if __name__ == '__main__':
	nums = [1,2,3]
	S = Solution()
	print S.subsets(nums)
	#rst = [list(i) for i in list(itertools.combinations(nums,1))]
	