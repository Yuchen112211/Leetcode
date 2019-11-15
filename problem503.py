class Solution(object):
	def nextGreaterElements(self, nums):
		import heapq
		stack = [nums[-1]]
		maxElement = max(nums)
		arr = [-1] * len(nums)
		for i in range(len(nums)-2, -1, -1):
			while stack:
				if stack[0] <= nums[i]:
					heapq.heappop(stack)
					heapq.heapify(stack)
				else:
					break
			if not stack:
				arr[i] = -1
			else:
				arr[i] = stack[0]
			heapq.heappush(stack, nums[i])
		return arr
if __name__ == '__main__':
	s = Solution()
	nums = [1,1,3]
	print s.nextGreaterElements(nums)