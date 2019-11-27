'''

131. Palindrome Partitioning
Medium

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

Solution:
Use recursion to solve the problem. 
For every input string, we can find out every parlindrome start at the head of the string, then call the same function to compute
the parlindrome cut of the remaining part of the string.

Remember, if the s is an empty string, we need to return [[]], not [], otherwise the situation when s itself as a parlindrome would
be missed.

Do not call another helper method to help verify parlindrome, just do it during the iteration, use helper method would cost a lot of time.

'''
class Solution(object):
	def partition(self, s):
		"""
		:type s: str
		:rtype: List[List[str]]
		"""
		if not s:
			return [[]]
		if len(s) == 1:
			return [[s]]
		if len(s) == 2:
			if s[0] == s[1]:
				return [[s[0],s[1]], [s]]
			else:
				return [[s[0],s[1]]]

		rst = []
		for i in range(1, len(s)+1):
			if s[:i] == s[:i][::-1]:
				for partition in self.partition(s[i:]):
					tmp = [s[:i]] + partition
					rst.append(tmp)
		return rst

s = Solution()
S = "aaa"
print s.partition(S)