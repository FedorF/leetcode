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
    if len(xs) == 0:
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


def find_longest_zigzag_length(root: Optional[TreeNode]) -> int:
    """

    Time complexity: O()
    Space complexity: O(1)

    """

    def dfs(tree: TreeNode, left: int = 0, right: int = 0):
        nonlocal max_length
        max_length = max(max_length, left, right)
        if tree.left:
            dfs(tree.left, right + 1, 0)
        if tree.right:
            dfs(tree.right, 0, left + 1)

    max_length = 0
    dfs(root)
    return max_length


if __name__ == '__main__':
    tree = build_tree([1, 1, 1, None, 1, None, None, 1, 1, None, 1])
    actual, expected = find_longest_zigzag_length(tree), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    tree = build_tree([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1])
    actual, expected = find_longest_zigzag_length(tree), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_longest_zigzag_length(build_tree([1])), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
