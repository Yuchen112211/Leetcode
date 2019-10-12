class Solution(object):

    def find_index(self,nums,value):
        for i in range(len(nums)):
            if value < nums[i]:
                return i
        return len(nums)
    
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        import bisect
        insert = []
        nums_rst = []
        nums.reverse()
        for i in nums:
            #index_tmp = bisect.bisect_left(nums_rst,i)
            index_tmp = self.find_index(nums_rst,i)
            insert.append(index_tmp)
            nums_rst.insert(index_tmp,i)
        insert.reverse()
        return insert

if __name__ == '__main__':
    s = Solution()
    print s.countSmaller([5,2,6,1])
