"""
Problem : 217. Contains Duplicate
Difficulty: Easy
Topics   : Array, Hash Table, Sorting
Runtime  : 3
Memory   : 32144000
Language : python3
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # counter = {}

        # for n in nums:
        #     counter[n] = counter.get(n, 0) + 1
        
        # for n in nums:
        #     if counter[n] > 1:
        #         return True
        
        # return False

        # seen = set()

        # for n in nums:
        #     if n in seen:
        #         return True
        #     else:
        #         seen.add(n)
        
        # return False

        return len(nums) != len(set(nums))
