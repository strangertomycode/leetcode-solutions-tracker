"""
Problem : 70. Climbing Stairs
Difficulty: Easy
Topics   : Math, Dynamic Programming, Memoization
Runtime  : 0
Memory   : 19256000
Language : python3
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        p1, p2 = 1, 1
        
        for i in range(n-1):
            temp = p2
            p2 = p2 + p1
            p1 = temp
        
        return p2
