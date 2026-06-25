"""
Problem : 67. Add Binary
Difficulty: Easy
Topics   : Math, String, Bit Manipulation, Simulation
Runtime  : 0
Memory   : 19460000
Language : python3
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # Start at the last character of string a
        i = len(a) - 1

        # Start at the last character of string b
        j = len(b) - 1

        carry = 0
        res = []

        while i >= 0 or j >= 0 or carry:

            # Get the current digit from a
            # If we've gone past the beginning, use 0
            digitA = int(a[i]) if i >= 0 else 0

            # Get the current digit from b
            # If we've gone past the beginning, use 0
            digitB = int(b[j]) if j >= 0 else 0

            # Add both digits and the carry
            total = digitA + digitB + carry

            # The current binary digit is:
            # total % 2
            #
            # Examples:
            # 0 % 2 = 0
            # 1 % 2 = 1
            # 2 % 2 = 0
            # 3 % 2 = 1
            #
            # Convert it to a string and save it
            res.append(str(total % 2))

            # Calculate the new carry
            carry = total // 2

            # Move one step left in string a
            i -= 1

            # Move one step left in string b
            j -= 1

        return ''.join(res[::-1])
