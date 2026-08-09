# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        if root is None:
            raise ValueError("root cannot be None")
    
        lowest_diff = abs(target - root.val)
        value_with_lowest = root.val
        def dfsb(node: TreeNode):
            nonlocal lowest_diff, value_with_lowest

            if node is None:
                return
            
            diff = abs(target - node.val)
            if lowest_diff is None or diff <= lowest_diff:
                lowest_diff = diff 
                value_with_lowest = node.val
            
          
            dfsb(node.left)
            dfsb(node.right)
           
        dfsb(root)

        return value_with_lowest



