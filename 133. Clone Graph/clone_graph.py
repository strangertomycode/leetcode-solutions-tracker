"""
Problem : 133. Clone Graph
Difficulty: Medium
Topics   : Hash Table, Depth-First Search, Breadth-First Search, Graph Theory
Runtime  : 42
Memory   : 19936000
Language : python3
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        oldToNew = {}

        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            else:
                copy = Node(node.val)
                oldToNew[node] = copy

                for n in node.neighbors:
                    copy.neighbors.append(clone(n))
                
                return copy
        
        return clone(node)
