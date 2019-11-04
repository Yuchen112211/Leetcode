class Solution(object):
	def nthUglyNumber(self, n, a,b,c):
		"""
		:type n: int
		:rtype: int
		"""
		
		
		import heapq
		cur_list = []
		
		heapq.heappush(cur_list,1)
		visited = set()
	
		result = 1
		
		while result <= n:
			cur = heapq.heappop(cur_list)
			if cur not in visited:
				visited.add(cur)
				result += 1
				for ele in (a,b,c):
					heapq.heappush(cur_list, cur*ele)
		
		return cur
		
		
		

if __name__ == '__main__':
	s = Solution()
	print s.nthUglyNumber(5,2,11,13)