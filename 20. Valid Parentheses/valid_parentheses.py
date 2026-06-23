"""
Problem : 20. Valid Parentheses
Difficulty: Easy
Topics   : String, Stack
Runtime  : 0
Memory   : 19376000
Language : python3
"""

class Solution:
    def isValid(self, s: str) -> bool:
        parantheses_map = {
            ")" : "(",
            "}" : "{",
            "]" : "[",
        }

        stack = []

        for p in s:
            if p in parantheses_map:
                if stack and stack[-1] == parantheses_map[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        
        return len(stack) == 0
        
