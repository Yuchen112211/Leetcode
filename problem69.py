class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        index = 0
        while index < x:

            if index * index >= x:
                return index - 1
            else:
                index += 1
        return index - 1

if __name__ == '__main__':
    x = Solution()
    print x.mySqrt(2)