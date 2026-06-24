"""
Problem : 53. Maximum Subarray
Difficulty: Medium
Topics   : Array, Divide and Conquer, Dynamic Programming
Runtime  : 31
Memory   : 31516000
Language : python3
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSum = max(maxSum, curSum)
        
        return maxSum
