"""
Problem : 150. Evaluate Reverse Polish Notation
Difficulty: Medium
Topics   : Array, Math, Stack
Runtime  : 2
Memory   : 20780000
Language : python3
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {"+", "-", "*", "/"}
        stack = []

        for t in tokens:
            if t in operators:
                o2 = stack.pop()
                o1 = stack.pop()

                if t == "+":
                    stack.append(o1 + o2)
                elif t == "-":
                    stack.append(o1 - o2)
                elif t == "*":
                    stack.append(o1 * o2)
                elif t == "/":
                    stack.append(int(o1 / o2))
            else:
                stack.append(int(t))
        
        return stack[-1]
                
