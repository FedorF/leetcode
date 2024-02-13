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


def delete_node(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    """

    Time complexity: O()
    Space complexity: O()

    """
    if not root:
        return root

    if key > root.val:  # continue search in the right subtree
        root.right = delete_node(root.right, key)

    elif key < root.val:  # continue search in the left subtree
        root.left = delete_node(root.left, key)

    else:  # found node to delete
        if root.left is None:
            return root.right

        if root.right is None:
            return root.left

        # find minimum node of right subtree
        right_min_node = root.right
        while right_min_node.left:
            right_min_node = right_min_node.left

        # assign right subtree minimum value to node we need to delete
        root.val = right_min_node.val

        # delete minimum node of right subtree
        root.right = delete_node(root.right, right_min_node.val)

    return root


if __name__ == '__main__':
    actual, expected = delete_node(build_tree([5, 3, 6, 2, 4, None, 7]), 3).to_list(), [5, 4, 6, 2, None, None, 7]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = delete_node(build_tree([5, 3, 6, 2, 4, None, 7]), 0).to_list(), [5, 3, 6, 2, 4, None, 7]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = delete_node(build_tree([]), 0), None
    assert actual == expected, f"expected: {expected}, actual: {actual}"
