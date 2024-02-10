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


def find_each_level_rightmost_nodes(root: Optional[TreeNode]) -> List[int]:
    """

    Time complexity: O(n_nodes)
    Space complexity: O(n_nodes)

    """

    def dfs(tree: TreeNode = root, level: int = 0):
        if tree is None:
            return

        if len(res) == level:
            res.append(tree.val)

        dfs(tree.right, level + 1)
        dfs(tree.left, level + 1)

    res = []
    dfs()
    return res


if __name__ == '__main__':
    actual, expected = find_each_level_rightmost_nodes(build_tree([1, 2, 3, None, 5, None, 4])), [1, 3, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_each_level_rightmost_nodes(build_tree([1, None, 3])), [1, 3]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_each_level_rightmost_nodes(build_tree([])), []
    assert actual == expected, f"expected: {expected}, actual: {actual}"
