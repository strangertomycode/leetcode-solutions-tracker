"""
Problem : 1. Two Sum
Difficulty: Easy
Topics   : Array, Hash Table
Runtime  : 3
Memory   : 20332000
Language : python3
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        n = len(nums)

        for i in range(n):
            rem = target - nums[i]
            if rem in num_map:
                return [num_map[rem], i]
            else:
                num_map[nums[i]] = i
