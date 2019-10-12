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