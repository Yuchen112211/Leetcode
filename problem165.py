'''
Very easy, gonna skip.
'''
class Solution(object):
	def compareVersion(self, version1, version2):
		"""
		:type version1: str
		:type version2: str
		:rtype: int
		"""
		strings1 = version1.split('.')
		strings2 = version2.split('.')
		rst1 = rst2 = 0
		length = max(len(strings1),len(strings2))
		for i in range(len(strings1)):
			rst1 += int(strings1[i])*pow(10,length - i)
		for i in range(len(strings2)):
			rst2 += int(strings2[i]) * pow(10,length - i)
		if rst1 < rst2:
			return -1
		elif rst1 == rst2:
			return 0
		else:
			return 1

if __name__ == '__main__':
	s = Solution()
	version1 = '0.4'
	version2 = '1.4'
	print s.compareVersion(version1,version2)