'''

315. Count of Smaller Numbers After Self
Hard

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

Solution:

Use the bisect.bisect_left, should solve this problem very easy.

'''

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
            index_tmp = bisect.bisect_left(nums_rst,i)
            #index_tmp = self.find_index(nums_rst,i)
            insert.append(index_tmp)
            nums_rst.insert(index_tmp,i)
        insert.reverse()
        return insert

if __name__ == '__main__':
    s = Solution()
    print s.countSmaller([5,2,6,1])
