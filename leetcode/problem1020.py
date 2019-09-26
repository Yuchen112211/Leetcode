class Solution(object):
	def numEnclaves(self, A):
		"""
		:type A: List[List[int]]
		:rtype: int
		"""
		stack = []
		for i in range(len(A)):
			for k in range(len(A[0])):
				if i == 0 or i == len(A)-1 or k == 0 or k == len(A[0])-1:
					if A[i][k] == 1:
						stack.append((i,k))
		while stack:
			i,k = stack.pop()
			A[i][k] = 0
			if i > 0:
				if A[i-1][k] == 1:
					stack.append((i-1,k))
			if i < len(A)-1:
				if A[i+1][k] == 1:
					stack.append((i+1,k))
			if k > 0:
				if A[i][k-1] == 1:
					stack.append((i,k-1))
			if k < len(A[0])-1:
				if A[i][k+1] == 1:
					stack.append((i,k+1))

		all_num = []
		for i in A:
			all_num += i
		return all_num.count(1)
		
if __name__ == '__main__':
	s = Solution()
	A = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
	print s.numEnclaves(A)