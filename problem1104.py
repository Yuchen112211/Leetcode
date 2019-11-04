class Solution(object):
	def pathInZigZagTree(self, label):
		"""
		:type label: int
		:rtype: List[int]
		"""
		if label == 1:
			return [1]
		rows = 0
		while True:
			if pow(2,rows) > label:
				break
			rows += 1
		rows -= 1
		offset = pow(-1,rows % 2)
		rst = [label]
		index_now = 0
		if rows % 2 == 0:
			index_now = label
		else:
			index_now = pow(2,rows+1)-label + pow(2,rows) - 1
		offset = -1 * offset
		rows -= 1
		while index_now != 1:
			if index_now % 2 == 1:
				next_index = (index_now - 1) / 2
			else:
				next_index = (index_now) / 2
			if rows % 2 == 0:
				val = next_index
			else:
				val = pow(2,rows) + pow(2,rows+1) - next_index-1
			rows -= 1
			index_now = next_index
			rst.append(val)
		rst.reverse()
		return rst

if __name__ == '__main__':
	s = Solution()
	s.pathInZigZagTree(31)