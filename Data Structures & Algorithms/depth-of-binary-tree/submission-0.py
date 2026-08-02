# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, i):
            if not node:
                return i
            depth = max(dfs(node.left, i + 1), dfs(node.right, i + 1))
            return depth
  
        return dfs(root, 0)