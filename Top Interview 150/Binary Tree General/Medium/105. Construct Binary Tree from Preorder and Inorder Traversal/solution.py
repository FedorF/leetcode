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


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    """
    1. Preorder traversal starts with root, then goes to left sub-tree, and finally goes to the right sub-tree.
    So, first element in preorder is always going to be a root value.
    2. Inorder traversal start with left subtree, then goes to root and finally to right sub-tree.

    Algorithm:
    Let's say preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]

    1. preorder[0] = 3 is a root.
    2. Now we want to know elements from left subtree. So, let's find 3 in the inorder list:

     [9,     |3|,   15, 20, 7]
    [left]   |root|   [ right ]

    We partitioned inorder: 3 is a root, all values to the left belong to left sub-tree, and values to the right belong
    to the right sub-tree.


    Time Complexity: O()
    Space Complexity: O()

    """
    if not preorder or not inorder:
        return None

    root = TreeNode(val=preorder[0])
    mid = inorder.index(root.val)
    root.left = build_tree(preorder[1:mid + 1], inorder[:mid])
    root.right = build_tree(preorder[mid + 1:], inorder[mid + 1:])
    return root


if __name__ == '__main__':
    actual = build_tree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7]).to_list()
    expected = [3, 9, 20, None, None, 15, 7]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual = build_tree(preorder=[-1], inorder=[-1]).to_list()
    expected = [-1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
