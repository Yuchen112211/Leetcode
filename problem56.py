'''

56. Merge Intervals
Medium

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Solution:
Sort the intervals by its first address/index, then go over the intervals.
If the interval at i has a middle start index between the recorded interval(index),
then update the interval at index, update its end index with the i's end index, and repeat.

If not, simply add the interval into rst, move the index to the next one.

Single iteration would solve the problem. Remember to check if current index is at the tail.

'''
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        def f(x):
            return x[0],x[1]

        intervals = sorted(intervals,key=f)
        index = 0
        rst = []
        while index < len(intervals):
            if index == len(intervals)-1:
                rst.append(intervals[index])
                break
            for i in range(index+1,len(intervals)):
                if intervals[index][0] <= intervals[i][0] <= intervals[index][1]:
                    intervals[index][1] = intervals[i][1]
                    if i == len(intervals)-1:
                        rst.append(intervals[index])
                        return rst
                else:
                    rst.append(intervals[index])
                    index = i
                    break
        return rst

if __name__ == '__main__':
    I = [[1,3],[2,6],[8,10],[15,18]]
    s = Solution()
    print s.merge(I)