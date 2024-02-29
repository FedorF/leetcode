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


def is_equal(xs: Optional[TreeNode], ys: Optional[TreeNode]) -> bool:
    """

    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """
    if not xs and not ys:
        return True

    if xs and not ys:
        return False

    if not xs and ys:
        return False

    if xs.val != ys.val:
        return False

    return is_equal(xs.left, ys.left) and is_equal(xs.right, ys.right)


if __name__ == '__main__':
    xs, ys = build_tree([1, 2, 3]), build_tree([1, 2, 3])
    actual, expected = is_equal(xs, ys), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs, ys = build_tree([1, 2]), build_tree([1, None, 2])
    actual, expected = is_equal(xs, ys), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs, ys = build_tree([1, 2, 1]), build_tree([1, 1, 2])
    actual, expected = is_equal(xs, ys), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
