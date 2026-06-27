"""
Problem : 14. Longest Common Prefix
Difficulty: Easy
Topics   : Array, String, Trie
Runtime  : 0
Memory   : 19224000
Language : python3
"""

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # Take the first word as our reference.
        first = strs[0]

        for i in range(len(first)):

            # Compare the current character with every other word.
            for word in strs[1:]:

                if i == len(word) or first[i] != word[i]:

                    # Return everything before this position.
                    #
                    # Example:
                    # first = "flower"
                    # i = 2
                    #
                    # first[:2] -> "fl"
                    return first[:i]
        return first
