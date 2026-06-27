"""
Problem : 338. Counting Bits
Difficulty: Easy
Topics   : Dynamic Programming, Bit Manipulation
Runtime  : 3
Memory   : 20100000
Language : python3
"""

class Solution:
    def countBits(self, n: int) -> List[int]:
        # res = []

        # for num in range(n + 1):
        #     count = 0
        #     while num > 0:
        #         rem = num % 2
        #         if rem == 1:
        #             count += 1
        #         num = num // 2
        #     res.append(count)
        
        # return res

        dp = [0] * (n + 1)

        for num in range (1, n+1):
            dp[num] = dp[num // 2] + (num % 2)
        
        return dp
