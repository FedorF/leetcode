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


def calc_path_based_numbers_sum(root: Optional[TreeNode]) -> int:
    """
    DFS Approach.


    Time complexity: O(n_nodes)
    Space complexity: O(n_nodes)

    """
    res = 0

    def dfs(node: TreeNode = root, number: int = 0):
        if not node.left and not node.right:
            nonlocal res
            res += number * 10 + node.val
            return

        if node.left:
            dfs(node.left, number * 10 + node.val)

        if node.right:
            dfs(node.right, number * 10 + node.val)

    dfs()
    return res


if __name__ == '__main__':
    actual, expected = calc_path_based_numbers_sum(build_tree([100])), 100
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_path_based_numbers_sum(build_tree([1, 2, 3])), 25
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_path_based_numbers_sum(build_tree([4, 9, 0, 5, 1])), 1026
    assert actual == expected, f"expected: {expected}, actual: {actual}"
