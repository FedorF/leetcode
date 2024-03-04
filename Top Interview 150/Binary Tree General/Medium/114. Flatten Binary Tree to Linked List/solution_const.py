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


def flatten(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """

    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """
    cur = root
    while cur:
        if cur.left:
            prev = cur.left
            while prev.right:
                prev = prev.right  # go to left sub-tree's right_most node

            prev.right = cur.right  # make current node's right sub-tree prev's right sub-tree
            cur.right = cur.left  # make it right sub-tree
            cur.left = None  # remove left

        cur = cur.right


if __name__ == '__main__':
    xs = build_tree([1, 2, 5, 3, 4, None, 6])
    flatten(xs)

    actual, expected = xs.to_list(), [1, None, 2, None, 3, None, 4, None, 5, None, 6]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_tree([])
    flatten(xs)
    actual, expected = xs, []
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    xs = build_tree([0])
    flatten(xs)
    actual, expected = xs.to_list(), [0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
