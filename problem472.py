'''

472. Concatenated Words
Hard
Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.

A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

Solution:
Use trie to solve the catenate words.
There may be too many repeated iteration in `if catenate(trie, word[i:]`).
So we use memorization, make the rst list, which is the result that we should return in this problem, to a set.

First we sort the words list by their length, this would somehow ensure that we do not miss any possibility of catenation.

In each iteration, go through the trie, when we find current letter is some word's end character, we first determine if the word that start from the current
letter is in the rst, if so, we are done, this word is a catenation of existing word. If not, call the function recursively, pass the word start
from current index to the method. If returned true, then this word is a catenation of the whole list.

Go through the iteration from head to tail of every word, if not a catenation, add the word into the trie.

'''

class Solution(object):
	def findAllConcatenatedWordsInADict(self, words):
		"""
		:type words: List[str]
		:rtype: List[str]
		"""
		_end = '_end_'
		def addTrie(trie, word):
			root = trie
			for letter in word:
				root = root.setdefault(letter, {})
			root[_end] = _end
			return root

		def catenate(trie, word):
			root = trie
			for i in range(len(word)):
				if _end in root:
					if word[i:] in rst:
						return True
					if catenate(trie, word[i:]):
						return True
				if word[i] in root:
					root = root[word[i]]
				else:
					return False

			if _end in root:
				return True
			else:
				return False

		while '' in words:
			words.remove('')
		if not words:
			return []
		words = sorted(words, key=lambda x:len(x))
		trie = {}
		rst = set([])
		addTrie(trie, words[0])
		for i in range(1, len(words)):
			if not catenate(trie, words[i]):
				addTrie(trie, words[i])
			else:
				rst.add(words[i])
		return list(rst)

s = Solution()
words =["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print s.findAllConcatenatedWordsInADict(words)