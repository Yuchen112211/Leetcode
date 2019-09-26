class Solution(object):
	def compute(self,l,sig):
		operation = ['*','/','+','-']
		tmp = l[0]
		for i in range(1,len(l)):
			if operation[i-1] == '*':
				tmp *= l[i]
			elif operation[i-1] == '/':
				tmp /= l[i]
			elif operation[i-1] == '+':
				if sig == 0:
					tmp += l[i]
				else:
					tmp -= l[i]
		return tmp

	def clumsy(self, N):
		length = N
		nums = ([N-i for i in range(length)])
		groups = length/4+1
		nums_compute = []
		for i in range(groups):
			nums_compute.append(nums[i*4:(i+1)*4])
		if [] in nums_compute:
			nums_compute.remove([])
		rst = self.compute(nums_compute[0],0)
		if len(nums_compute) == 1:
			return rst
		else:
			for i in range(1,len(nums_compute)):
				rst -= self.compute(nums_compute[i],1)
		return rst

if __name__ == '__main__':
	s = Solution()
	#s.compute([6,5,4,3])
	print s.clumsy(4)
