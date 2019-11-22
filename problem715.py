'''

715. Range Module
Hard

A Range Module is a module that tracks ranges of numbers. Your task is to design and implement the following interfaces in an efficient manner.

addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.

queryRange(int left, int right) Returns true if and only if every real number in the interval [left, right) is currently being tracked.

removeRange(int left, int right) Stops tracking every real number currently being tracked in the interval [left, right).

Example 1:

addRange(10, 20): null
removeRange(14, 16): null
queryRange(10, 14): true (Every number in [10, 14) is being tracked)
queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not being tracked)
queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked, despite the remove operation)

Solution:
The trick here is using problem#57 insert interval.
remember left = right = [] would cause copy error.


'''
class RangeModule(object):

    def __init__(self):
        self.ranges = []
        

    def addRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        if not self.ranges:
            self.ranges.append([left, right])
        newInterval = [left, right]
        left = []
        right = []
        for interval in self.ranges:
            if interval[0] < newInterval[0] and interval[1] < newInterval[0]:
                left.append(interval)
            elif interval[0] > newInterval[1] and interval[1] > newInterval[1]:
                right.append(interval)
            else:
                if interval[0] < newInterval[0]:
                    newInterval[0] = interval[0]
                if interval[1] > newInterval[1]:
                    newInterval[1] = interval[1]

        self.ranges = sorted(left + [newInterval] + right, key=lambda x:x[0])

    def queryRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: bool
        """
        for interval in self.ranges:
            if interval[0] <= left < right <= interval[1]:
                return True
        return False
        

    def removeRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: None
        """
        rst = []
        for interval in self.ranges:
            if right < interval[0] or left > interval[1]:
                rst.append(interval)
            elif left <= interval[0] < interval[1] <= right:
                continue
            elif interval[0] < left <= interval[1] <= right:
                rst.append([interval[0], left])
            elif left <= interval[0] <= right <= interval[1]:
                rst.append([right, interval[1]])
            elif interval[0] < left < right < interval[1]:
                rst.append([interval[0], left])
                rst.append([right, interval[1]])
        self.ranges = sorted(rst, key=lambda x: x[0])

# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
obj.addRange(10,20)
obj.removeRange(14,16)
print obj.queryRange(10,14)
print obj.queryRange(13,15)
print obj.queryRange(16,17)
print obj.ranges