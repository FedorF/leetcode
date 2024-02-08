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


def leaf_equal(xs: Optional[TreeNode], ys: Optional[TreeNode]) -> bool:
    """

    Time complexity: O(n)
    Space complexity: O(n_leafs)

    """

    def find_leafs(node: TreeNode):
        if node is None:
            return []

        if node.left is None and node.right is None:  # found leaf
            return [node.val]

        return find_leafs(node.left) + find_leafs(node.right)

    xs, ys = find_leafs(xs), find_leafs(ys)
    if len(xs) != len(ys):
        return False

    for i in range(len(xs)):
        if xs[i] != ys[i]:
            return False

    return True


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


if __name__ == '__main__':
    xs = build_tree([1, 2])
    ys = build_tree([2, 2])
    actual, expected = leaf_equal(xs, ys), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_tree([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4])
    ys = build_tree([3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
    actual, expected = leaf_equal(xs, ys), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_tree([1, 2, 3])
    ys = build_tree([1, 3, 2])
    actual, expected = leaf_equal(xs, ys), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
