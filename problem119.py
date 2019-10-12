class Solution(object):
	def getRow(self, rowIndex):
		"""
		:type rowIndex: int
		:rtype: List[int]
		"""
		if rowIndex == 0:
			return [1]
		else:
			last = self.getRow(rowIndex-1)
			now = [1]
			for i in range(len(last)-1):
				now.append(last[i]+last[i+1])
			now.append(1)
		return now

if __name__ == '__main__':
	s = Solution()
	print s.getRow(3)