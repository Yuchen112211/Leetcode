'''

738. Monotone Increasing Digits
Medium

Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x <= y.)

Example 1:

Input: N = 10
Output: 9

Example 2:

Input: N = 1234
Output: 1234

Example 3:

Input: N = 332
Output: 299

Solution:
Pure math problem, complicated and pointless.

'''
class Solution(object):
	def monotoneIncreasingDigits(self, N):
		"""
		:type N: int
		:rtype: int
		"""
		digits = [int(i) for i in str(N)]
		index = -1
		for i in range(len(digits)-1):
			if digits[i] <= digits[i+1]:
				continue
			else:
				index = i+1
				digits[i] -= 1
				break
		rst = (len(digits) - index) * '9'
		if index == -1:
			return N
		index -= 1
		while index > 0:
			if digits[index] < digits[index - 1]:
				digits[index] = 9
				digits[index-1] -= 1
			index -= 1
		length = len(rst)
		for i in range(len(digits) - length-1, -1, -1):
			rst = str(digits[i]) + rst
		return int(rst)
		


		
s = Solution()
N = 120000

print s.monotoneIncreasingDigits(N)