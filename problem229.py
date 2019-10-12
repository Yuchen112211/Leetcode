class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num1,num2 = 0,0
        cnt1,cnt2 = 0,0
        index = 0
        while index < len(nums):
        	if nums[index] == num1:
        		cnt1 += 1
        	elif nums[index] == num2:
        		cnt2 += 1
        	elif cnt1 == 0:
        		num1 = nums[index]
        		cnt1 = 1
        	elif cnt2 == 0:
        		num2 = nums[index]
        		cnt2 = 1
        	else:
        		cnt1 -= 1
        		cnt2 -= 1
        	index += 1
        cnt1,cnt2 = 0,0
        index = 0
        while index < len(nums):
        	if nums[index] == num1:
        		cnt1 += 1
        	if nums[index] == num2:
        		cnt2 += 1
        	index += 1
        rst = set()
        if cnt1 > len(nums)/3.0:
        	rst.add(num1)
        if cnt2 > len(nums)/3.0:
        	rst.add(num2)
        return list(rst)


if __name__ == '__main__':
	S = Solution()
	print S.majorityElement([3,2,3])