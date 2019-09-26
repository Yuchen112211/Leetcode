class Solution(object):
	def generateMatrix(self, n):
		"""
		:type n: int
		:rtype: List[List[int]]
		"""
		import copy
		directions = ['r','d','l','u']
		d_cnt = 0
		matrix = [[0 for i in range(n)] for k in range(n)]
		matrix[0][0] = 1
		cnt = 1
		indexes = [0,0]
		while cnt < n*n:
			current_d = directions[d_cnt % 4]
			next_index = copy.deepcopy(indexes)
			if current_d == 'r':
				next_index[1] += 1
			elif current_d == 'd':
				next_index[0] += 1
			elif current_d == 'l':
				next_index[1] -= 1
			elif current_d == 'u':
				next_index[0] -= 1
			if next_index[0] < 0 or next_index[1] < 0 or next_index[0] >= n or next_index[1] >= n:
				d_cnt += 1
				continue
			elif matrix[next_index[0]][next_index[1]] != 0:
				d_cnt += 1
				continue
			else:
				matrix[next_index[0]][next_index[1]] = cnt+1
				cnt += 1
				indexes = copy.deepcopy(next_index)

		return matrix
if __name__ == '__main__':
	s = Solution()
	n = 2
	rst = s.generateMatrix(n)
	for i in rst:
		print i