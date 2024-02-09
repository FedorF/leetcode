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


def count_target_path_sum(root: Optional[TreeNode], target: int) -> int:
    """
    DFS approach.
    Start path from every node. Use boolean variable to distinguish new route and existing route continuation.


    Time complexity: O(n^2) ???
    Space complexity: O(1)

    """

    def dfs(tree: TreeNode, cur_sum: int, path_start: bool):
        nonlocal counter
        if tree is None:
            return

        if tree.left is None and tree.right is None:
            if path_start and tree.val == target:
                counter += 1

            elif cur_sum + tree.val == target:
                counter += 1

            return

        if path_start:
            if tree.val == target:
                counter += 1

            # start from current
            dfs(tree.left, tree.val, False)
            dfs(tree.right, tree.val, False)

            # start from children
            dfs(tree.left, 0, True)
            dfs(tree.right, 0, True)
            return

        # not a starting node of new path
        if cur_sum + tree.val == target:
            counter += 1

        # continue path
        dfs(tree.left, cur_sum + tree.val, False)
        dfs(tree.right, cur_sum + tree.val, False)

    counter = 0
    dfs(root, 0, True)
    return counter


if __name__ == '__main__':
    actual, expected = count_target_path_sum(build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    tree = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    actual, expected = count_target_path_sum(tree, 22), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_target_path_sum(build_tree([]), 100), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_target_path_sum(build_tree([1]), 1), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
