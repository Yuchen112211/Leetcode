class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        min_distance = max([min([abs(k-i) for k in heaters]) for i in houses])
        return min_distance

if __name__ == '__main__':
    houses,heaters = [1,2,3,4],[1,4]
    s = Solution()
    print s.findRadius(houses,heaters)
