class Solution(object):
	def find132pattern(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		if len(nums) < 3:
			return False
		minV = [nums[0]]
		heap = []
		import heapq
		for i in range(1,len(nums)):
			minV.append(min(minV[-1], nums[i]))
		for i in range(len(nums)-1,-1,-1):
			while heap:
				if heap[0] <= minV[i]:
					heapq.heappop(heap)
				else:
					break
			if heap:
				if nums[i] > heap[0] > minV[i]:
					return True
			heapq.heappush(heap, nums[i])
		return False
s = Solution()
nums = [1,0,1,-3,-4]

print s.find132pattern(nums)