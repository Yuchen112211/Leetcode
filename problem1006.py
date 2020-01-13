'''
1006. Clumsy Factorial
Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.  For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial: using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations: multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However, these operations are still applied using the usual order of operations of arithmetic: we do all multiplication and division steps before any addition or subtraction steps, and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.  This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.


Example 1:

Input: 4
Output: 7
Explanation: 7 = 4 * 3 / 2 + 1

Example 2:

Input: 10
Output: 12
Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

 

Note:

    1 <= N <= 10000
    -2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)


Solution:
After observing the examples, I noticed that every four numbers can form a group.
Each group is connected with the minus operator.

So if input is 5, which is (5 * 4 / 3 + 2) - (1)
When computing, split every 4 numbers in one group, and compute them.

With the helper Method compute, we can ignore how many numbers are in each group, which can
let us ignore the last group with less than 4 numbers.

Can be optimized. Stacks? Still going as four operators.

'''

class Solution(object):
	def compute(self,l,sig):
		operation = ['*','/','+','-']
		tmp = l[0]
		for i in range(1,len(l)):
			if operation[i-1] == '*':
				tmp *= l[i]
			elif operation[i-1] == '/':
				tmp /= l[i]
			elif operation[i-1] == '+':
				if sig == 0:
					tmp += l[i]
				else:
					tmp -= l[i]
		return tmp

	def clumsy(self, N):

		length = N
		nums = ([N-i for i in range(length)])
		groups = length/4+1
		nums_compute = []

		for i in range(groups):
			nums_compute.append(nums[i*4:(i+1)*4])

		if [] in nums_compute:
			nums_compute.remove([])

		rst = self.compute(nums_compute[0],0)
		#Can be optimized
		if len(nums_compute) == 1:
			return rst
		else:
			for i in range(1,len(nums_compute)):
				rst -= self.compute(nums_compute[i],1)
		return rst

if __name__ == '__main__':
	s = Solution()
	#s.compute([6,5,4,3])
	print s.clumsy(4)
