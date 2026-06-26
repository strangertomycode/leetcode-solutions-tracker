"""
Problem : 13. Roman to Integer
Difficulty: Easy
Topics   : Hash Table, Math, String
Runtime  : 5
Memory   : 19436000
Language : python3
"""

class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        # This will store our final answer
        total = 0

        for i in range(len(s)):

            # Is there another character after this one?
            if i + 1 < len(s):

                # Is the next Roman numeral larger?
                if roman[s[i]] < roman[s[i + 1]]:

                    # Then subtract this value
                    total -= roman[s[i]]

                else:

                    # Otherwise add it
                    total += roman[s[i]]

            else:
                # Last character has no next character,
                # so just add it.
                total += roman[s[i]]

        return total
