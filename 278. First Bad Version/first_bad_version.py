"""
Problem : 278. First Bad Version
Difficulty: Easy
Topics   : Binary Search, Interactive
Runtime  : 44
Memory   : 19028000
Language : python3
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 1
        r = n
        res = 0

        while l <= r:
            m = (l + r) // 2

            if isBadVersion(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        
        return res

