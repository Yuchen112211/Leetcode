'''

1052. Grumpy Bookstore Owner
Medium

Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers (customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1, otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

 

Example 1:

Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], X = 3
Output: 16
Explanation: The bookstore owner keeps themselves not grumpy for the last 3 minutes. 
The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

Solution:

Sliding window solution, instead of compute and determine whether the grumpy is 1, we simply form
the list by multiply corresbonding element in customers and grumpy.

In this way we can save some time and space for the problem.
'''

class Solution(object):
	def maxSatisfied(self, customers, grumpy, X):
		if X >= len(grumpy) or sum(grumpy) == 0:
			return sum(customers)
		tmp = [0 if x == 1 else 1 for x in grumpy]
		potential = [a*b for a,b in zip(customers,grumpy)]
		guaranteed = sum([a*b for a,b in zip(customers,tmp)])

		if X == 0:
			return guaranteed
		curr = sum(potential[0:X])
		res = curr
		l = 0

		for r in range(X, len(potential)):
			curr -= potential[l]
			curr += potential[r]
			res = max(res, curr)
			l += 1
		return res + guaranteed

if __name__ == '__main__':
	s = Solution()
	customers = [1,0,1,2,1,1,7,5]
	grumpy = [0,1,0,1,0,1,0,1]
	X = 3
	print s.maxSatisfied(customers, grumpy, X)