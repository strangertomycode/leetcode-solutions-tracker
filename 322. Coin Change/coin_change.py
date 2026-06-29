"""
Problem : 322. Coin Change
Difficulty: Medium
Topics   : Array, Dynamic Programming, Breadth-First Search
Runtime  : 464
Memory   : 19452000
Language : python3
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0

        for current_amount in range (1, amount + 1):
            for coin in coins:
                if coin <= current_amount:
                    dp[current_amount] = min(dp[current_amount], dp[current_amount - coin] + 1)
        
        if dp[amount] == float("inf"):
            return -1
        
        return dp[amount]
