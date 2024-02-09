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


def count_good_nodes(root: Optional[TreeNode]) -> int:
    """
    DFS approach.


    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """

    def dfs(tree: TreeNode, path_max_val: int):
        nonlocal counter
        if tree is None:
            return

        if tree.left is None and tree.right is None:  # found leaf
            if tree.val >= path_max_val:
                counter += 1
            return

        if tree.val >= path_max_val:
            path_max_val = tree.val
            counter += 1

        dfs(tree.left, path_max_val)
        dfs(tree.right, path_max_val)
        return

    counter = 0
    dfs(root, root.val)
    return counter


if __name__ == '__main__':
    actual, expected = count_good_nodes(build_tree([3, 1, 4, 3, None, 1, 5])), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_good_nodes(build_tree([3, 3, None, 4, 2])), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_good_nodes(build_tree([1])), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
