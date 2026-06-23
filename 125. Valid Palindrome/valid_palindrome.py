"""
Problem : 125. Valid Palindrome
Difficulty: Easy
Topics   : Two Pointers, String
Runtime  : 3
Memory   : 20708000
Language : python3
"""

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(cleaned_s)
        return cleaned_s == cleaned_s[::-1]
