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


def find_k_smallest(root: Optional[TreeNode], k: int) -> int:
    """
    DFS Approach. Apply in-order traversal.
    (See Readme.md)


    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """
    def dfs(node):
        nonlocal found_min, k, res
        if k < 0:  # already found
            return

        if not node:
            if not found_min:  # found minimal value
                k -= 1
                found_min = True
            return

        dfs(node.left)  # start left search
        if k == 0:
            res = node.val
            k -= 1
            return

        k -= 1
        dfs(node.right)  # start right search
        return

    found_min = False
    res = None

    dfs(root)
    return res


if __name__ == '__main__':
    actual, expected = find_k_smallest(build_tree([3, 1, 4, None, 2]), 1), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_k_smallest(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"
