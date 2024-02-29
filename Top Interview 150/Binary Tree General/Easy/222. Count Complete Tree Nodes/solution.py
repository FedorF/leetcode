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
    DFS Approach.


    Time complexity: O()
    Space complexity: O()

    """


if __name__ == '__main__':
    actual, expected = count_nodes(build_tree([1, 2, 3, 4, 5, 6])), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_nodes(build_tree([10])), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_nodes(build_tree([])), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
