'''

516. Longest Palindromic Subsequence
Medium

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"

Output:

4

One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:

"cbbd"

Output:

2

One possible longest palindromic subsequence is "bb". 

Solution:
Now we first see that, to determine parlindrome, one way is to reverse it, see if it is the same as the original string.
So as for the parlindrome subsequence, we can reverse the original string, then find the longest common subsequence of the two strings.

Since the latter one is reversed version of the original string, once there is a common subsequence, its length is the longest possible
parlidrome subsequence's length.

This solution is incredibly slow. DP should be fast? Maybe there's some better solutions.

'''

class Solution(object):
	def longestCommonSubseq(self, s1, s2):
		dp = [[0 for i in range(len(s1) + 1)] for k in range(len(s2) + 1)]

		for i in range(len(s1)):
			for k in range(len(s2)):
				if s1[i] == s2[k]:
					dp[i+1][k+1] = dp[i][k] + 1
				else:
					dp[i+1][k+1] = max(dp[i+1][k], dp[i][k+1])
		return dp[-1][-1]

	def longestPalindromeSubseq(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if not s:
			return 0
		s1 = s
		s2 = s[::-1]
		return self.longestCommonSubseq(s1,s2)

s = Solution()
s1 = 'cbbd'
print s.longestPalindromeSubseq(s1)