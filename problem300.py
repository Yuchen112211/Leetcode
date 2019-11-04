class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = right = 0
        max_length = 0
        while right < len(nums)-1:
        	if nums[right] <= nums[right+1]:
        		right += 1
        	else:
        		print nums[left:right+1]
        		max_length = max(max_length,right-left+1)
        		right += 1
        		left = right
        return max_length
        
if __name__ == '__main__':
	nums = [10,9,2,5,3,7,101,18]
	S = Solution()
	print S.lengthOfLIS(nums)