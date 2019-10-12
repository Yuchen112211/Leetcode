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


