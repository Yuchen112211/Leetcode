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