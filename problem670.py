'''

670. Maximum Swap
Medium

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: 9973
Output: 9973
Explanation: No swap.

Solution:
First find out if the start digit is the biggest digit and there's a same digit in the following
characters, if so, move on, if not, break the loop.
This step also pass through the digit that is the biggest digit in the remaining digits.
Actually this step is essential and creative.

Then we have passed every digits that we should not change, then we find out the biggest digit 
from the tail to head, if find 9, break, else we check if the first element is the biggest one.
If so, it means we jumped over the whole sequence, so return the original number.

'''
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num <= 10:
            return num
        str_num = str(num)
        length = len(str_num)
        index = length-1
        biggest = '0'
        start = 0
        while start < length:
            if max(str_num[start:]) == str_num[start]:
                start += 1
            else:
                break
        if start == length:
            return num
        for i in range(1,length-start):
            if str_num[length-i] > biggest:
                biggest = str_num[length-i]
                index = length-i
            if biggest == '9':
                break
        if index == length-1 and str_num[index] < str_num[start]:
            return num
        rst = str_num[:start]+str_num[index]+str_num[start+1:index]+str_num[start]+str_num[index+1:]
        return int(rst)

if __name__ == '__main__':
    s = Solution()
    num = 99712
    print s.maximumSwap(num)