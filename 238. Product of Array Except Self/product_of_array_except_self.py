"""
Problem : 238. Product of Array Except Self
Difficulty: Medium
Topics   : Array, Prefix Sum
Runtime  : 19
Memory   : 25516000
Language : python3
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]
        
        return answer
