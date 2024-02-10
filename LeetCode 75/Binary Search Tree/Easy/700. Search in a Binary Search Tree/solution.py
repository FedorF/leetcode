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


def find_node(root: Optional[TreeNode], val: int) -> List[int]:
    """

    Time complexity: O(log(n_nodes))
    Space complexity: O(1)

    """

    def dfs(tree: TreeNode = root):
        if tree is None:
            return

        if tree.val == val:
            return tree

        if val < tree.val:
            return dfs(tree.left)

        else:
            return dfs(tree.right)

    return dfs()


if __name__ == '__main__':
    actual, expected = find_node(build_tree([4, 2, 7, 1, 3]), 2).to_list(), [2, 1, 3]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_node(build_tree([4, 2, 7, 1, 3]), 5), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"
