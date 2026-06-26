"""
Problem : 543. Diameter of Binary Tree
Difficulty: Easy
Topics   : Tree, Depth-First Search, Binary Tree
Runtime  : 3
Memory   : 22196000
Language : python3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(curr):
            if not curr:
                return 0
            
            hl = dfs(curr.left)
            hr = dfs(curr.right)

            self.res = max(self.res, hl + hr)

            return 1 + max(hl, hr)
        dfs(root)
        return self.res

