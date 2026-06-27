"""
Problem : 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Topics   : Hash Table, String, Sliding Window
Runtime  : 15
Memory   : 19180000
Language : python3
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        left = 0
        longest = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])

            longest = max(longest, right - left + 1)
        
        return longest
