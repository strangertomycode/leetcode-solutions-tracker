"""
Problem : 844. Backspace String Compare
Difficulty: Easy
Topics   : Two Pointers, String, Stack, Simulation
Runtime  : 0
Memory   : 19316000
Language : python3
"""

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        first, second = [], []

        for c in s:
            if c == "#":
                if first:                    
                    first.pop()
            else:
                first.append(c)
        
        for c in t:
            if c == "#":
                if second:
                    second.pop()
            else:
                second.append(c)
        
        return first == second
