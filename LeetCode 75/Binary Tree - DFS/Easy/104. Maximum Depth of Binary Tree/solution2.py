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


def calc_tree_depth(tree: Optional[TreeNode]) -> int:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """

    def dfs(root: Optional[TreeNode] = tree, depth: int = 0) -> int:
        if not root:
            return depth

        return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))

    return dfs()


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
    actual, expected = calc_tree_depth(build_tree([3, 9, 20, None, None, 15, 7])), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_tree_depth(build_tree([1, None, 2])), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_tree_depth(build_tree([1])), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_tree_depth(build_tree([])), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
