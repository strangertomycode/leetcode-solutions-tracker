"""
Problem : 973. K Closest Points to Origin
Difficulty: Medium
Topics   : Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect
Runtime  : 74
Memory   : 25440000
Language : python3
"""

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)

        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res
