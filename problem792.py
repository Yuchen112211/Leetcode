class Solution(object):
	def numMatchingSubseq(self, S, words):

		number = 0
		indexes = {}
		for i in range(len(S)):
			currentCharacter = indexes.setdefault(S[i],[])
			currentCharacter.append(i)
		for word in words:
			currentIndex = -1
			isSub = True
			for i in range(len(word)):
				if word[i] not in indexes:
					isSub = False
					break
				else:
					has = False
					for k in range(len(indexes[word[i]])):
						if indexes[word[i]][k] > currentIndex:
							currentIndex = indexes[word[i]][k]
							has = True
							break
					if not has:
						isSub = False
						break
			number += isSub
		return number


s = Solution()

S = "abcde"
words = ["a", "bb", "acd", "ace"]

print s.numMatchingSubseq(S, words)