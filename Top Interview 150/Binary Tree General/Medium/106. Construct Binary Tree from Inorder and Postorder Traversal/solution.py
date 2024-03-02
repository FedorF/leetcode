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


def build_tree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    """
    1. Inorder traversal start with left subtree, then goes to root and finally to right sub-tree.
    2. Postorder traversal starts with left sub-tree, then goes to right sub-tree, and finally goes to the root.
    So, last element in postorder list is always going to be a root value.

    Algorithm:
    Let's say inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]

    1. postorder[-1] = 3 is a root.
    2. Now we want to know elements from right subtree. So, let's find 3 in the inorder list:

     [9,     |3|,   15, 20, 7]
    [left]   |root|   [ right ]

    We partitioned inorder: 3 is a root, all values to the left belong to left sub-tree, and values to the right belong
    to the right sub-tree.


    Time Complexity: O()
    Space Complexity: O()

    """
    if not inorder or not postorder:
        return None

    root = TreeNode(val=postorder.pop())
    mid = inorder.index(root.val)
    root.right = build_tree(inorder[mid + 1:], postorder)
    root.left = build_tree(inorder[:mid], postorder)

    return root


if __name__ == '__main__':
    actual = build_tree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3]).to_list()
    expected = [3, 9, 20, None, None, 15, 7]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual = build_tree(inorder=[-1], postorder=[-1]).to_list()
    expected = [-1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
