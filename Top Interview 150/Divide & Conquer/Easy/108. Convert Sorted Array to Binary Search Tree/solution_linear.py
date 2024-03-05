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


def build_binary_search_tree(nums: List[int]) -> Optional[TreeNode]:
    """
    DFS approach.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    def build(xs: List[int]) -> Optional[TreeNode]:
        if not xs:
            return

        mid = len(xs) // 2
        tree = TreeNode(val=xs[mid], left=build(xs[:mid]), right=build(xs[mid + 1:]))
        return tree

    return build(nums)


if __name__ == '__main__':
    actual, expected = build_binary_search_tree([-10, -3, 0, 5, 9]).to_list(), [0, -3, 9, -10, None, 5, None]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = build_binary_search_tree([1, 3]).to_list(), [3, 1, None]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = build_binary_search_tree([]), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"
