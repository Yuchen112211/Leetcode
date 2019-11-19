'''

821. Shortest Distance to a Character
Easy

Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]

 

Note:

    S string length is in [1, 10000].
    C is a single character, and guaranteed to be in string S.
    All letters in S and C are lowercase.

Solution:
Record one index, compare it with the substring that starts at iteration index i to the
end of the whole String.

Update the index whenever encounter another C.

'''
class Solution(object):
	def shortestToChar(self, S, C):
		rst = []
		current_length = S.index(C)
		for i in range(len(S)):
			if S[i] == C:
				current_length = i
				rst.append(0)
			else:
				if C in S[i:]:
					if abs(i-current_length) < S[i:].index(C):
						rst.append(i-current_length)
					else:
						rst.append(S[i:].index(C))
				else:
					rst.append(i-current_length)

		return rst
		
if __name__ == '__main__':
	s = Solution()
	S = "loveleetcode"
	C = 'e'
	print s.shortestToChar(S,C)


