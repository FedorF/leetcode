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


def validate_binary_search_tree(root: Optional[TreeNode]) -> bool:
    """
    DFS Approach.


    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """

    def dfs(node: TreeNode, min_val: Optional[int] = None, max_val: Optional[int] = None) -> bool:
        if not node:
            return True

        if (max_val is not None) and (node.val >= max_val):
            return False

        if (min_val is not None) and (node.val <= min_val):
            return False

        if not dfs(node.left, min_val, node.val):  # check left sub-tree
            return False

        return dfs(node.right, node.val, max_val)  # check right sub-tree

    return dfs(root)


if __name__ == '__main__':
    actual, expected = validate_binary_search_tree(build_tree([2, 1, 3])), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = validate_binary_search_tree(build_tree([5, 1, 4, None, None, 3, 6])), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
