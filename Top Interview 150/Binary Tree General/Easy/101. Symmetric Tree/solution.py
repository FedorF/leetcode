from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(xs: List[int]) -> Optional[TreeNode]:
    if not xs:
        return

    def build(ind: int = 0) -> TreeNode:
        if ind >= len(xs) or xs[ind] is None:
            return

        node = TreeNode(xs[ind])
        node.left = build(2 * ind + 1)
        node.right = build(2 * ind + 2)
        return node

    tree = build()
    return tree


def is_symmetric(root: Optional[TreeNode]) -> bool:
    """
    DFS Approach.


    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """
    if not root:
        return True

    def dfs(left_node, right_node):
        if not left_node and not right_node:
            return True

        if not left_node and right_node:
            return False

        if left_node and not right_node:
            return False

        if left_node.val != right_node.val:
            return False

        return dfs(left_node.left, right_node.right) and dfs(right_node.left, left_node.right)

    return dfs(root.left, root.right)


if __name__ == '__main__':
    actual, expected = is_symmetric(build_tree([1, 2, 2, 3, 4, 4, 3])), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = is_symmetric(build_tree([1, 2, 2, None, 3, None, 3])), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
