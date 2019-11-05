'''

1124. Longest Well-Performing Interval
Medium

We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

 

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].


'''


class Solution:
	def longestWPI(self, hours):
		Sum, ans = 0, 0
		cache = {}
		for i, n in enumerate(hours):
			Sum = Sum + 1 if n > 8 else Sum - 1
			if Sum > 0: ans = i + 1
			if Sum-1 in cache:
				ans = max(ans, i - cache[Sum-1])
			cache.setdefault(Sum, i)
		return ans

		
if __name__ == '__main__':
	s = Solution()
	hourst = [9,9,6,0,6,6,9]