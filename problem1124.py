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

Solution:
This is a dp problem. Initialize two variables, Sum and ans.

Iterate all through the hours(the given list), if current hour is bigger than 8, plus 1 to sum, else minus 1 to sum.

Then we see whether the sum is bigger than 0. If so, which means current day is still in a well-performing interval.
So we add 1 to ans.

If the sum is less than 0, which means the well-performing interval has come to the end, which means the day with more
than 8 hours is currently equal or less than the days with no more than 8. If the sum-1 is in the cache, which means there
is a well-performing ending before. Make the ans to be the biggest of current length and ans.

The Sum - 1 is that where is the start of the last valid well-performing index starts. When current Sum is 1, we need to find 
whether 0 is in the cache, and compute the longest well-performing interval.

cache.setdefault is similar to dict d[Sum] = i.

The i would give us the information about where the well-performing interval starts.
'''


class Solution:
	def longestWPI(self, hours):
		Sum, ans = 0, 0
		cache = {}
		for i, n in enumerate(hours):
			Sum = Sum + 1 if n > 8 else Sum - 1
			if Sum > 0:
				ans = i + 1
			if Sum - 1 in cache:
				ans = max(ans, i - cache[Sum-1])
			cache.setdefault(Sum, i)
		return ans

		
if __name__ == '__main__':
	s = Solution()
	hourst = [9,9,6,0,6,6,9]
	print s.longestWPI(hourst)