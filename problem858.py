'''

The reflection problem.
Pure math question.

Flip the square, if we flip it one time, then the length is p * 2, and we can only reach 0.
If we flip if two time, then the length is p * 3, we can reach 1 and 2, simply compute the odd-even relationship between p * 3 and q.

So from this, we know just find the number k to multiply p so that can divide q by whole. Then find out the k is even or odd.

'''
class Solution(object):
	def mirrorReflection(self, p, q):
		"""
		:type p: int
		:type q: int
		:rtype: int
		"""
		num = 1
		while p * num % q:
			num += 1
		if num % 2:
			return 2 - (p * num / q) % 2
		else:
			return 0

s = Solution()
print s.mirrorReflection(2,1)