class Solution(object):
	def minimumDeleteSum(self,s1,s2):
		import collections
		count_s1 = collections.Counter(s1)
		count_s2 = collections.Counter(s2)

		return count_s2,count_s1
if __name__ == '__main__':
	s = Solution()
	s1 = 'delete'
	s2 = 'leet'
	print s.minimumDeleteSum(s1,s2)