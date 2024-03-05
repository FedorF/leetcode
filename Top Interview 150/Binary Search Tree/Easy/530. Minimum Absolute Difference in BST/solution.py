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


def calc_nodes_abs_min_diff(root: Optional[TreeNode]) -> int:
    """
    DFS Approach. Similar with "98. Validate Binary Search Tree" approach.
    Keep track on minimal and maximum values on each node.


    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """

    def dfs(node: TreeNode = root, min_val: Optional[int] = None, max_val: Optional[int] = None):
        nonlocal res
        if not node:
            return

        if (min_val is not None) and abs(node.val - min_val) < res:
            res = abs(node.val - min_val)

        if (max_val is not None) and abs(node.val - max_val) < res:
            res = abs(node.val - max_val)

        dfs(node.left, min_val, node.val)
        dfs(node.right, node.val, max_val)
        return

    res = float('inf')
    dfs()
    return res


if __name__ == '__main__':
    actual, expected = calc_nodes_abs_min_diff(build_tree([0, None, 2236, 1277, 2776, 519])), 519
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_nodes_abs_min_diff(build_tree([4, 2, 6, 1, 3])), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_nodes_abs_min_diff(build_tree([1, 0, 48, None, None, 12, 49])), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
