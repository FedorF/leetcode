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


def traverse_zigzag_by_level(root: Optional[TreeNode]) -> List[List[int]]:
    """
    BFS iterative approach.


    Time complexity: O(n_nodes)
    Space complexity: O(n_nodes)

    """
    if not root:
        return []

    res = []
    queue = deque([root])
    level = 0
    while queue:
        nodes = [0] * len(queue)  # predefine nodes list
        for i in range(len(queue)):
            node = queue.popleft()
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

            if level % 2 > 0:  # fill nodes list straightly
                nodes[i] = node.val
            else:  # fill nodes list reversely
                nodes[-i - 1] = node.val

        res.append(nodes)
        level += 1

    return res


if __name__ == '__main__':
    actual, expected = traverse_zigzag_by_level(build_tree([3, 9, 20, None, None, 15, 7])), [[3], [20, 9], [15, 7]]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = traverse_zigzag_by_level(build_tree([1])), [[1]]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = traverse_zigzag_by_level(build_tree([])), []
    assert actual == expected, f"expected: {expected}, actual: {actual}"
