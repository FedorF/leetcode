from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


def calc_levels_avg(root: Optional[TreeNode]) -> List[float]:
    """
    BFS approach.

    Time complexity: O(n_nodes)
    Space complexity: O(n_nodes)

    """
    res = []
    queue = deque([root])
    while queue:
        n_nodes = len(queue)
        level_sum = 0
        for i in range(n_nodes):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        res.append(level_sum / n_nodes)

    return res


if __name__ == '__main__':
    actual, expected = calc_levels_avg(build_tree([3, 9, 20, None, None, 15, 7])), [3, 14.5, 11]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_levels_avg(build_tree([3, 9, 20, 15, 7])), [3, 14.5, 11]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
