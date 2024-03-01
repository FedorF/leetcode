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


def calc_max_path_sum(root: Optional[TreeNode]) -> int:
    """
    DFS Approach.

    At each node we could either:
    1) make a split using current node as a "knot"
    2) or calculate left and right sub-trees sums and pass it up


    Time complexity: O(n)
    Space complexity: O(1)

    """
    max_sum = root.val

    def dfs(node: TreeNode = root):
        nonlocal max_sum
        if not node.left and not node.right:  # found a leaf
            max_sum = max(max_sum, node.val)
            return node.val

        left_sum = right_sum = 0
        if node.left:
            left_sum = max(left_sum, dfs(node.left))

        if node.right:
            right_sum = max(right_sum, dfs(node.right))

        # consider making a split on the current node
        max_sum = max(max_sum, node.val + left_sum + right_sum)

        # return best sub-tree sum
        return max(node.val, left_sum + node.val, right_sum + node.val)

    dfs()
    return max_sum


if __name__ == '__main__':
    actual, expected = calc_max_path_sum(build_tree([1, 2, 3])), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_path_sum(build_tree([-10, 9, 20, None, None, 15, 7])), 42
    assert actual == expected, f"expected: {expected}, actual: {actual}"
