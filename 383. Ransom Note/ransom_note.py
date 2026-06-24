"""
Problem : 383. Ransom Note
Difficulty: Easy
Topics   : Hash Table, String, Counting
Runtime  : 22
Memory   : 19664000
Language : python3
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = {}

        for c in magazine:
            count[c] = count.get(c, 0) + 1
        
        for c in ransomNote:
            if count.get(c, 0) <=0:
                return False
            else:
                count[c] -= 1
        
        return True
