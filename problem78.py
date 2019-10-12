import itertools

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
        	print rst
        return rst



if __name__ == '__main__':
	nums = [1,2,3]
	S = Solution()
	print S.subsets(nums)
	#rst = [list(i) for i in list(itertools.combinations(nums,1))]
	