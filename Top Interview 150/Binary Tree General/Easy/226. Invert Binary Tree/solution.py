from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        self.repr = []

    def to_list(self):
        if self.repr:
            return self.repr

        xs = []
        queue = [self]
        while queue:
            copy = queue[:]
            queue = []
            for node in copy:
                if node is None:
                    xs.append(None)
                    queue.append(None)
                    queue.append(None)
                else:
                    xs.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if all(x is None for x in queue):
                break

        return xs


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


def invert_binary_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """

    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """
    if not root:
        return

    root.left, root.right = invert_binary_tree(root.right), invert_binary_tree(root.left)
    return root


if __name__ == '__main__':
    xs = build_tree([4, 2, 7, 1, 3, 6, 9])
    actual, expected = invert_binary_tree(xs).to_list(), [4, 7, 2, 9, 6, 3, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_tree([2, 1, 3])
    actual, expected = invert_binary_tree(xs).to_list(), [2, 3, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_tree([])
    actual, expected = invert_binary_tree(xs), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"
