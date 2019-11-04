class Solution(object):
	def maxSlidingWindow(self, nums, k):
		'''
		import collections
		d = collections.deque()
		out = []
		for i,n in enumerate(nums):
			while d and nums[d[-1]] < n:
				d.pop()
			d += i,
			if d[0] == i-k:
				d.popleft()
			if i >= k - 1:
				out += nums[d[0]],
		return out
		'''
		if not nums:
			return []
		cnt = collections.defaultdict(int)
		heap = []
		for i in range(k):
			heapq.heappush(heap,-nums[i])
		res = [-heap[0]]
		for i in range(1,len(nums)-k+1):
			heapq.heappush(heap,-nums[i+k-1])
			cnt[-nums[i-1]] += 1
			while cnt[heap[0]] > 0:
				cnt[heap[0]] -= 1
				heapq.heappop(heap)
			res += [-heap[0]]
		return res
		
if __name__ == '__main__':
	window = [1,3,-1,-3,5,3,6,7]
	s = Solution()
	print s.maxSlidingWindow(window,3)