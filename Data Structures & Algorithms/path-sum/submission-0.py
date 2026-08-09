# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def has_sum_path(node, current_sum):
            if not node:
                return False
            current_sum = node.val + current_sum
            if not node.left and not node.right and current_sum == targetSum:
                return True

            return has_sum_path(node.left, current_sum ) or has_sum_path(node.right, current_sum )




        return has_sum_path(root, 0)