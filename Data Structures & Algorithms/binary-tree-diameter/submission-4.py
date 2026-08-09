# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(node):
            if not node:
                return 0, 0  # height, diameter

            left_height, left_diameter = solve(node.left)
            right_height, right_diameter = solve(node.right)

            height = 1 + max(left_height, right_height)

            diameter_through_node = left_height + right_height

            diameter = max(
                diameter_through_node,
                left_diameter,
                right_diameter
            )

            return height, diameter

        _, diameter = solve(root)
        return diameter

        