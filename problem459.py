'''

459. Repeated Substring Pattern
Easy

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. 
You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

 

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.

Example 2:

Input: "aba"
Output: False

Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

Solution:
Remember to move the validation len(s) % len(word) into the iteration so that to find the 
correct substring.

'''
class Solution(object):
	def repeatedSubstringPattern(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		if not s:
			return True
		word = ''
		for i in range(len(s)/2, -1, -1):
			if s[i+1:].startswith(s[:i+1]):
				if len(s) % len(s[:i+1]):
					continue
				word = s[:i+1]
				break

		if not word:
			return False
		if len(s) % len(word):
			return False
		times = len(s) / len(word)
		for i in range(times):
			if s[i * len(word):(i+1) * len(word)] != word:
				return False
		return True

if __name__ == '__main__':
	s = Solution()
	x = "ababababab"

	print s.repeatedSubstringPattern(x)