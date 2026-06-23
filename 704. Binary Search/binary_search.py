"""
Problem : 704. Binary Search
Difficulty: Easy
Topics   : Array, Binary Search
Runtime  : 0
Memory   : 20512000
Language : python3
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l<=r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1
