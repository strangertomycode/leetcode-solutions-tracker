"""
Problem : 242. Valid Anagram
Difficulty: Easy
Topics   : Hash Table, String, Sorting
Runtime  : 15
Memory   : 19440000
Language : python3
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h_s = {}
        h_t = {}

        if len(s) != len(t):
            return False

        else:
            for i in range(len(s)):
                if s[i] in h_s:
                    h_s[s[i]] += 1
                else:
                    h_s[s[i]] = 1
                if t[i] in h_t:
                    h_t[t[i]] += 1
                else:
                    h_t[t[i]] = 1
        
        return h_s == h_t
