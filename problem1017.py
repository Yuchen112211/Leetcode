class Solution(object):
	def baseNeg2(self, N):
		"""
		:type N: int
		:rtype: str
		"""
		from collections import deque

		def add_in(d,i):
			if i % 2 == 1:
				if i + 1 in d:
					d.remove(i+1)
					add_in(d, i+2)
				else:
					d.add(i+1)
			if i in d:
				d.remove(i)
				add_in(d, i+1)
			else:
				d.add(i)
				
		if N == 0:
			return "0"
		number = N
		digit = deque([])
		
		

		while number != 0:
			index = 0
			while pow(2,index) <= number:
				index += 1
			if index > 0:
				index -= 1
			digit.append(index)
			number = number % pow(2, index)
		rst = set([])

		for i in digit:
			add_in(rst,i)

		print rst

		res = ""
		for i in range(max(rst),-1,-1):
			if i in rst:
				res += "1"
			else:
				res += "0"
		return res

if __name__ == '__main__':
	s = Solution()
	N = 14
	print s.baseNeg2(N)
