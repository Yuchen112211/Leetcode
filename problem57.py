'''

57. Insert Interval
Hard

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Solution:
Not too difficult, wonder why this question is hard.
Problem 56 may be more difficult. This question's difference is only we need to add a new interval.
Find where the newInterval would be fitting. 

In the iteration, check two situations:
1. If the newInterval is on the left or right of the Interval.
2. If there's overlap between two intervals.

'''
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        left = []
        right = []
        for interval in intervals:
            if interval[0] < newInterval[0] and interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1] and interval[1] > newInterval[1]:
                right.append(interval)
            
            else:
                if interval[0] < newInterval[0]:
                    newInterval[0] = interval[0]
                if interval[1] > newInterval[1]:
                    newInterval[1] = interval[1]
        return left + [newInterval] + right
		
if __name__ == '__main__':
	s = Solution()
	intervals = [[1,3],[7,9]]
	newInterval = [5,6]
	print s.insert(intervals,newInterval)