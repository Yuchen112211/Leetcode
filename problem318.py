'''
318. Maximum Product of Word Lengths
Medium

Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".

Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".

Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.


Solution:
Valuable Approach!
To determine whether two strings has common characters, we can transform them both into binary form.
First convert all characters to be interger, we can use 1 << ord(string[k]) - ord('a'), then we add them 
together, then we have two numbers num1 and num2. every number would be 1 + 0 * n, and n equals to the 
corresbonding number of the character.

Use OR operation on the two numbers. If there's no common character, the OR operation should be:
num1 | num2 == num1 + num2.
Just think carefully and you'll see it why it works. If there's a common character, let's say 'ab' and 'ac',
'ab' equals to 1 + 10, 'ac' equals to 1 + 100, once there's a common character, the sum of the two number can
not be the same as num1 | num2, cause there's an or multiple '1' in the same place.

'''
class Solution(object):
	'''
	def containDuplicate(self,word1_set,word2):
		for i in word1_set:
			if i in word2:
				return True
		return False

	def maxProduct(self, words):
		words_length = ([len(i) for i in words])
		words_set = ([set(i) for i in words])
		max_rst = 0
		for i in range(len(words)-1):
			current_max_length = 0
			for k in range(i+1,len(words)):
				if current_max_length > words_length[k]:
					continue
				else:
					if self.containDuplicate(words_set[i],words[k]):
						continue
					else:
						current_max_length = words_length[k]
			max_rst = max(max_rst,words_length[i]*current_max_length)
		print max_rst
	'''
	def maxProduct(self, words):
		nums = [0 for i in words]
		words_length = [len(i) for i in words]
		max_length = 0
		for i in range(len(words)):
			word_set = set(words[i])
			for k in word_set:
				nums[i] += 1 <<(ord(k)-ord('a'))
		for i in range(len(words)-1):
			for k in range(i+1,len(words)):
				if (nums[i] | nums[k] )== (nums[i] + nums[k]):
					max_length = max(max_length,words_length[i]*words_length[k])
		return max_length

if __name__ == '__main__':
	s = Solution()
	words = ["abcw","baz","foo","bar","xtfn","abcdef"]
	words = ["a","aa","aaa","aaaa"]
	print s.maxProduct(words)