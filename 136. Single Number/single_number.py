"""
Problem : 136. Single Number
Difficulty: Easy
Topics   : Array, Bit Manipulation
Runtime  : 0
Memory   : 21076000
Language : python3
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            res ^= n
        return res
