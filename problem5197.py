'''

This is a contest problem, don't recal the specific problem.

'''
class Solution(object):
	def minimumAbsDifference(self, arr):
		"""
		:type arr: List[int]
		:rtype: List[List[int]]
		"""
		sorted(arr)
		rst = []
		for i in range(len(arr)-1):
			rst.append(arr[i+1]-arr[i])
		mini = min(rst)
		result = []
		for i in range(len(rst)):
			if rst[i] == mini:
				result.append([arr[i],arr[i+1]])
		return result

if __name__ == '__main__':
	arr = [1,3,6,10,15]
	s = Solution()
	print s.minimumAbsDifference(arr)