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
    Space complexity: O(1)
    
    """

    def build(left: int = 0, right: int = len(nums) - 1) -> TreeNode:
        if left > right:
            return

        mid = left + (right - left) // 2
        tree = TreeNode(val=nums[mid], left=build(left, mid - 1), right=build(mid + 1, right))
        return tree

    return build()


if __name__ == '__main__':
    actual, expected = build_binary_search_tree([-10, -3, 0, 5, 9]).to_list(), [0, -10, 5, None, -3, None, 9]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = build_binary_search_tree([1, 3]).to_list(), [1, None, 3]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = build_binary_search_tree([]), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"
