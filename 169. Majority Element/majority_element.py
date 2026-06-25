"""
Problem : 169. Majority Element
Difficulty: Easy
Topics   : Array, Hash Table, Divide and Conquer, Sorting, Counting
Runtime  : 4
Memory   : 21132000
Language : python3
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        # counter = {}

        # for n in nums:
        #     counter[n] = counter.get(n, 0) + 1
        
        # for n in nums:
        #     if counter[n] > len(nums)/2:
        #         return n

        candidate = None
        counter = 0

        for n in nums:
            if counter == 0:
                candidate = n
            if candidate == n:
                counter += 1
            else:
                counter -= 1
        
        return candidate
