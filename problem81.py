class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        index,move = 0,0
        if target == nums[0]:
            return True
        
        if target < nums[0]:
            index = -1
            move = -1
        if target > nums[0]:
            index = 0
            move = 1
        while abs(index) < len(nums):
            if nums[index] == target:
                return True
            index += move

        return False

if __name__ == '__main__':
    x = Solution()
    print x.search([2,5,6,0,0,1,2],3)