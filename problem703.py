'''

703. Kth Largest Element in a Stream
Easy

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

Solution:
This problem can be solved by min heap.
What I learned from this problem is, if not neccessary, do not use heapq.heapify, since it is O(n).
Use heappush and heappop instead, they only take O(lg n).

'''
import heapq

class KthLargest:

    def __init__(self, k, nums):
        heapq.heapify(nums)
        self.heap = nums
        self.k = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        if len(self.heap) >= self.k:
            if val < self.heap[0]:
                return self.heap[0]
            else:
                heapq.heappop(self.heap)
        heapq.heappush(self.heap, val)
        return self.heap[0]

# import heapq
# class KthLargest(object):

#     def __init__(self, k, nums):
#         """
#         :type k: int
#         :type nums: List[int]
#         """
#         self.sizes = k
#         self.heap = []
#         if len(nums) < k:
#             self.heap = nums
#             heapq.heapify(self.heap)
#             return
#         for i in range(k):
#             heapq.heappush(self.heap,nums[i])
#         for i in range(k, len(nums)):
#             if nums[i] > self.heap[0]:
#                 self.heap[0] = nums[i]
#                 heapq.heapify(self.heap)
            
#     def add(self, val):
#         """
#         :type val: int
#         :rtype: int
#         """
#         if len(self.heap) < self.sizes:
#             heapq.heappush(self.heap, val)
#             return self.heap[0]
#         if val > self.heap[0]:
#             self.heap[0] = val
#             heapq.heapify(self.heap)
#         return self.heap[0]