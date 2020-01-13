class Solution(object):
	def largeGroupPositions(self, S):
		"""
		:type S: str
		:rtype: List[List[int]]
		"""
		indexes = []
		character = "*"
		leftIndex = 0
		rightIndex = 0

		for i in range(len(S)):
			if S[i] != character:
				if rightIndex - leftIndex >= 2:
					indexes.append([leftIndex, rightIndex])
				character = S[i]
				leftIndex = i
				rightIndex = i
			else:
				rightIndex += 1
		if rightIndex - leftIndex >= 2:
			indexes.append([leftIndex, rightIndex])
		return indexes

s = Solution()
S = "aaa"

print s.largeGroupPositions(S)