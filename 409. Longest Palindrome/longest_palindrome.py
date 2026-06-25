"""
Problem : 409. Longest Palindrome
Difficulty: Easy
Topics   : Hash Table, String, Greedy
Runtime  : 0
Memory   : 19412000
Language : python3
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        # else:
        #     counter = {}
        #     res = 0
            
        #     for c in s:
        #         counter[c] = counter.get(c, 0) + 1
        #         if counter[c] % 2 == 0:
        #             res += 2

        #     for c in s:
        #         if counter[c] % 2 != 0:
        #             res += 1
        #             break

        # return res 

        else:
            visited = set()
            res = 0

            for c in s:
                if c in visited:
                    visited.remove(c)
                    res += 2
                else:
                    visited.add(c)
            
            if visited:
                res += 1
            return res

