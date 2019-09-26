class Solution(object):
	def maxSlidingWindow(self, nums, k):
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
		
if __name__ == '__main__':
	window = [1,3,-1,-3,5,3,6,7]
	s = Solution()
	print s.maxSlidingWindow(window,3)