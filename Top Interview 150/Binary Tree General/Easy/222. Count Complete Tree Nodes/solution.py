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


def count_nodes(root: Optional[TreeNode]) -> int:
    """
    DFS Approach:

    If left sub-tree height equals right sub-tree height then,
        a. left sub-tree is perfect binary tree
        b. right sub-tree is complete binary tree

    If left sub-tree height greater than right sub-tree height then,
        a. left sub-tree is complete binary tree
        b. right sub-tree is perfect binary tree


    Time complexity: O(log(n) ^ 2)
    Space complexity: O(1)

    """
    if not root:
        return 0

    def calc_depth_right(node: TreeNode, level: int = 0):
        if not node:
            return level

        return calc_depth_right(node.right, level + 1)

    def calc_depth_left(node: TreeNode, level: int = 0):
        if not node:
            return level

        return calc_depth_left(node.left, level + 1)

    left_depth = calc_depth_left(root.left)
    right_depth = calc_depth_right(root.right)

    if left_depth == right_depth:
        return 2 ** (left_depth + 1) - 1

    return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == '__main__':
    actual, expected = count_nodes(build_tree([1, 2, 3, 4, 5, 6])), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_nodes(build_tree([10])), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_nodes(build_tree([])), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
