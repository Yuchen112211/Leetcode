class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        arr = [0] * (amount + 1)
        index = 0
        arr[0] = 1
        while index < len(coins):
        	for i in range(amount+1):
        		if arr[i] != 0 and i + coins[index] < (amount+1):
        			arr[i+coins[index]] += arr[i]
        	index += 1
        return arr[-1]

s = Solution()
coins = [1,2,5]
s.change(100,coins)