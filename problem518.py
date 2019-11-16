'''

518. Coin Change 2
Medium

You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

 

Example 1:

Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:

Input: amount = 10, coins = [10] 
Output: 1

SolutionL
Another DP problem, only change is to find how many ways to form such amount of money by the coins,
which is like dungeon game, bottom-up algorithm.

'''
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