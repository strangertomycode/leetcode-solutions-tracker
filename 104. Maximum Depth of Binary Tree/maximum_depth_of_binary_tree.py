"""
Problem : 104. Maximum Depth of Binary Tree
Difficulty: Easy
Topics   : Tree, Depth-First Search, Breadth-First Search, Binary Tree
Runtime  : 2
Memory   : 20244000
Language : python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(curr):
            if not curr:
                return 0
            leftDepth = dfs(curr.left)
            rightDepth = dfs(curr.right)

            return 1 + max(leftDepth, rightDepth)

        return dfs(root)
