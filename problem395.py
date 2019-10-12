class Solution(object):
	def longestSubstring(self, s, k):
		"""
		:type s: str
		:type k: int
		:rtype: int
		"""
		if len(s) < k:
			return ''
		character_pos = {}
		character_cnt = {}
		for i in range(len(s)):
			if s[i] not in character_cnt:
				character_pos[s[i]] = [i]
				character_cnt[s[i]] = 1
			else:
				character_pos[s[i]].append(i)
				character_cnt[s[i]] += 1
		min_val = min(character_cnt.values())

		if min_val >= k:
			return s
		else:
			key = 0
			for i in character_pos:
				if character_cnt[i] == min_val:
					key = i
					break
			if len(character_pos[0]) == 1:

			for i in range(len(character_pos[i]) - 1):


		print character_cnt
		print character_pos



if __name__ == '__main__':
	Solution = Solution()
	s = 'aaabb'
	k = 3
	Solution.longestSubstring(s,k)