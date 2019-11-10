'''

279. Perfect Squares
Medium

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Solution:
Use dp.
Generating current number by iterating all sqaure number before.
Current_num is the possible base to fomating the current number.dp[i] = dp[i-k*k] because
from i-k*k to i we need only a k square to form i.
Dp solution here is very efficient and easy to understand.

'''
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