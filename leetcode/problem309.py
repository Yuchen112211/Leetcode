'''
Method 1: DP algorithm with O(n) time and O(1) space

For each day, there are 3 possible actions: buy, sell, nothing. Let us define
buy[i] = maxProfit of prices[:i+1] with the action buy at day i,
sell[i] = maxProfit of prices[:i+1] with the action sell at day i,
nothing[i] = maxProfit of prices[:i+1] with the action nothing at day i.

The base cases are buy[0] = -prices[0], sell[0] = nothing[0] = 0.
The recursive relationships are
buy[i] = max(nothing[i-1] - prices[i], buy[i-1]) # if buy at day i then the action at day i-1 must be nothing
sell[i] = max(buy[i-1]+prices[i], sell[i-1])
nothing[i] = max(sell[i-1], buy[i-1], nothing[i-1]).
'''
# Insightful approach
    def maxProfit(self, prices):
        if n < 2: 
            return 0
        prev_buy, prev_sell, prev_nothing = -prices[0], 0, 0
        for i in range(1, n):
            buy  = max(prev_nothing - prices[i], prev_buy) 
            sell = max(prev_buy + prices[i], prev_sell)
            nothing = max(prev_sell, prev_buy, prev_nothing)
            prev_buy, prev_sell, prev_nothing = buy, sell, nothing
        return max(sell, nothing)
