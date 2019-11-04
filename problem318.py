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
				nums[i] += 1<<(ord(k)-ord('a'))
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