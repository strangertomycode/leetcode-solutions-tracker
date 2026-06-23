"""
Problem : 121. Best Time to Buy and Sell Stock
Difficulty: Easy
Topics   : Array, Dynamic Programming
Runtime  : 71
Memory   : 28760000
Language : python3
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices) and l <= r:
            if prices[l] < prices[r]:
                d = prices[r] - prices[l]
                profit = max(profit, d)
            else:
                l = r
            r += 1
        
        return profit

