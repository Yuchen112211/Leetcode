'''

402. Remove K Digits
Medium

Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

	The length of num is less than 10002 and will be ≥ k.
	The given num does not contain any leading zero.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.

Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain leading zeroes.

Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.

Solution:
My original solution is to go over the whole list k times, for each time we find out the biggest number
from the beginning, we select the biggest number each time, after k time, the remaining should be the 
smallest number possibile.

It is very slow, may be optimized.

'''

'''
class Solution(object):
	def removeKdigits(self, num, k):
		if not num:
			return '0'
		if k >= len(num):
			return '0'
		while k > 0:
			maxIndex = 0
			for i in range(1,len(num)):
				if num[i] < num[i - 1]:
					maxIndex = i - 1
					break
				if i == len(num) - 1:
					maxIndex = i
			num = num[:maxIndex] +  num[maxIndex + 1:]
			k -= 1
		zeroIndex = 0
		for i in range(len(num)):
			if num[i] == '0':
				zeroIndex += 1
			else:
				break
		num = num[zeroIndex:]
		if not num:
			return "0"
		return num
'''

class Solution(object):
	def removeKdigits(self, num, k):
		if k >= len(num): return '0'
		num = [l for l in num]
		
		while k > 0:
			flag = True
			for i in range(len(num)-1):
				if str(num[i]) > str(num[i+1]):
					num.pop(i)
					k, flag = k - 1, False
					break
					
			if flag == True and num[i+1] == num[-1]: 
				num.pop(i+1)
				k -= 1
		
		return str(int(''.join(num)))

s = Solution()
num = "1432219"
k = 3
print s.removeKdigits(num, k)
			