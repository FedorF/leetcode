from collections import deque
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


def find_max_sum_level(root: Optional[TreeNode]) -> int:
    """

    Time complexity: O(n_nodes)
    Space complexity: O(n_nodes)

    """
    if root is None:
        return

    max_sum = root.val
    level = res = 1
    queue = deque([root])
    while queue:
        level_sum = 0
        for _ in range(len(queue)):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            res = level

        level += 1

    return res


if __name__ == '__main__':
    actual, expected = find_max_sum_level(build_tree([1, 7, 0, 7, -8, None, None])), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_max_sum_level(build_tree([989, None, 10250, 98693, -89388, None, None, None, -32127])), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_max_sum_level(build_tree([1000])), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
