"""
Problem : 102. Binary Tree Level Order Traversal
Difficulty: Medium
Topics   : Tree, Breadth-First Search, Binary Tree
Runtime  : 0
Memory   : 19960000
Language : python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []

            for i in range(len(q)):
                node = q.popleft()
                
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if level:
                res.append(level)
        
        return res
            

