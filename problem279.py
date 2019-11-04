class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            current_num = int(sqrt(i))+1
            dp[i] = min([dp[i-k*k] for k in range(current_num)]) + 1
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print s.numSquares(13)