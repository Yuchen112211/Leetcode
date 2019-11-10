'''

239. Sliding Window Maximum
Hard

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Solution:

Use the defaultdict of the collections, because this can automatically assign new key valud pair without
determine its existence.

Use the heapq, which would maintain a min heap.
This problem requires us to find out the max value of a window, then we'll store each element's reverse
value into the min heap, which would function as a max heap.

The cnt defaultdict represents the element that has passed. The element in the cnt will be added 1
only when the element is exactly before the window sliding.
When the max heap's head in cnt is bigger than 0, which means the max value of window before has passed, so
we use a while loop to pop out the max heap's head, the times of popping equals to the element count in cnt,
which means how many the number has passed.

Very elegent approach, very interesting.

'''
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
		import collections
		import heapq

		if not nums:
			return []
		cnt = collections.defaultdict(int)
		heap = []
		for i in range(k):
			heapq.heappush(heap,-nums[i])
		print heap
		res = [-heap[0]]
		for i in range(1,len(nums)-k+1):
			heapq.heappush(heap,-nums[i+k-1])
			cnt[-nums[i-1]] += 1
			while cnt[heap[0]] > 0:
				cnt[heap[0]] -= 1
				heapq.heappop(heap)
			print heap,cnt

			res += [-heap[0]]
		return res
		
if __name__ == '__main__':
	window = [1,3,-1,-3,5,3,6,7]
	#window = [3,3,3,3,3,3,3,3,3,3]

	s = Solution()
	print s.maxSlidingWindow(window,3)