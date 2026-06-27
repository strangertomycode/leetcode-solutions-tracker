"""
Problem : 191. Number of 1 Bits
Difficulty: Easy
Topics   : Divide and Conquer, Bit Manipulation
Runtime  : 3
Memory   : 19272000
Language : python3
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        while n:
            res += n % 2
            n = n // 2
        
        return res
