'''

127. Word Ladder
Medium

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

	Only one letter can be changed at a time.
	Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:

	Return 0 if there is no such transformation sequence.
	All words have the same length.
	All words contain only lowercase alphabetic characters.
	You may assume no duplicates in the word list.
	You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

Solution:

This is actually a very smart one.
We first form a dict, record each string as the forms with slashes.
For examples, ABC would become _BC,A_C,AB_, these as keys, and ABC as value.

Then we form the stack, first form the beginword into a tuple, where the second
value is one, means the distance.

Pop out what is in stack, if word is not used, then we find all its neighbors by the
procedures like before, we can find every string that follow this pattern.
If there's any word like this pattern did not appear before, add the distance by 1 and
push it back into the stack.

The element that popped out from the stack, we need to check whether it's the endword,
if so, return its distance, if not, continue the process
'''

class Solution(object):
	def ladderLength(self, beginWord, endWord, wordList):
		adj = collections.defaultdict(list)
		for word in wordList:
			for i in range(len(word)):
				adj[word[:i] + '_' + word[i+1:]].append(word)
		visited = set()
		q = collections.deque([(beginWord, 1)])
		while q:
			word, k = q.popleft()
			if word == endWord:
				return k
			if word not in visited:
				visited.add(word)
				for i in range(len(word)):
					neighbors = word[:i] + '_' + word[i+1:]
					for neighbor in adj[neighbors]:
						q.append((neighbor, k+1))
		return 0
			
			

if __name__ == '__main__':
	s = Solution()
	beginWord = "hit"

	endWord = 'cog'
	wordList = ["hot","dot","dog","lot","log","cog"]#wordList = ['hit','cog']
	val = s.ladderLength(beginWord,endWord,wordList)
	print val