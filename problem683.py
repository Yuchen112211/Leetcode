'''

683. K Empty Slots
Hard

You have N bulbs in a row numbered from 1 to N. Initially, all the bulbs are turned off. We turn on exactly one bulb everyday until all bulbs are on after N days.

You are given an array bulbs of length N where bulbs[i] = x means that on the (i+1)th day, we will turn on the bulb at position x where i is 0-indexed and x is 1-indexed.

Given an integer K, find out the minimum day number such that there exists two turned on bulbs that have exactly K bulbs between them that are all turned off.

If there isn't such day, return -1.

 

Example 1:

Input: 
bulbs: [1,3,2]
K: 1
Output: 2
Explanation:
On the first day: bulbs[0] = 1, first bulb is turned on: [1,0,0]
On the second day: bulbs[1] = 3, third bulb is turned on: [1,0,1]
On the third day: bulbs[2] = 2, second bulb is turned on: [1,1,1]
We return 2 because on the second day, there were two on bulbs with one off bulb between them.

Example 2:

Input: 
bulbs: [1,2,3]
K: 1
Output: -1

Solution:
Binary search to find the neighbors can be really helpful.

class Solution(object):
	def kEmptySlots(self, bulbs, K):
		"""
		:type bulbs: List[int]
		:type K: int
		:rtype: int
		"""
		import bisect
		result = [bulbs[0]]
		day = 1
		for i in range(1, len(bulbs)):
			day += 1
			index = bisect.bisect_left(result, bulbs[i])
			prevIndex = index - 1
			nextIndex = index
			if prevIndex >= 0:
				if bulbs[i] - result[prevIndex] - 1 == K:
					return day
			if nextIndex < len(result):
				if result[nextIndex] - bulbs[i] - 1 == K:
					return day
			result.insert(index,bulbs[i])
		return -1

The other solution we have here, is try to think this as a linked list.
Elegant solution.

We think the procedures of the insertion reversely, as removal of the bulbs. For each deletion of the bulb, we try to
see if the current removing bulb would give us an interval that has length K.

Update the left and right interval if needed, and the trick part is we modify the left and right and ans till the
end of the iteration, not simply return it. Update the left and right boarders with each removal, since with a 2-d
matrix we can easily locate the left node and right node.
'''

class Solution(object):
	def kEmptySlots(self, bulbs, k):
		garden = [[i - 1, i + 1] for i in range(len(bulbs))]
		garden[0][0], garden[-1][1] = None, None
		ans = -1
		for i in range(len(bulbs) - 1, -1, -1):
			cur = bulbs[i] - 1
			left, right = garden[cur]
			current = bulbs[i] - 1
			if right != None and right - cur == k + 1:
				ans = i + 1
			if left != None and cur - left == k + 1:
				ans = i + 1
			if right != None:
				garden[right][0] = left
			if left != None:
				garden[left][1] = right
		return ans

s = Solution()
bulbs = [1,2,4,5,3]
K = 1
print s.kEmptySlots(bulbs, K)