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


def has_path_sum(root: Optional[TreeNode], target: int) -> bool:
    """
    DFS Approach.


    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """
    if not root:
        return False

    def dfs(node: TreeNode = root, cur_sum: int = 0):
        if not node.left and not node.right:  # found leaf
            return cur_sum + node.val == target

        if node.left and dfs(node.left, cur_sum + node.val):  # check left subtree
            return True

        if node.right and dfs(node.right, cur_sum + node.val):  # check right subtree
            return True

        return False

    return dfs()


if __name__ == '__main__':
    actual, expected = has_path_sum(build_tree([1, 2]), 1), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = has_path_sum(build_tree([1, 2]), 0), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = has_path_sum(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = has_path_sum(build_tree([1, 2, 3]), 5), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = has_path_sum(build_tree([]), 0), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
