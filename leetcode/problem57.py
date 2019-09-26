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