"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        to_return = []
        def dfs(node):
            if not node:
                return
            for children in node.children:
                dfs(children)
            to_return.append(node.val)
        dfs(root)
        print(to_return)
        return to_return