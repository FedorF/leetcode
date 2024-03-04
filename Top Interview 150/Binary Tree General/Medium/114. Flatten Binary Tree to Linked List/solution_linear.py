from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def flatten(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """
    DFS approach.


    Time complexity: O(n_nodes)
    Space complexity: O(n_nodes)

    """
    stack = [root]
    while stack:
        node = stack.pop()
        if node.right:
            stack.append(node.right)

        if node.left:
            stack.append(node.left)

        node.left = None
        if stack:
            node.right = stack[-1]
