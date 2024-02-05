from typing import Optional


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.class_name = self.__class__.__name__

    def _to_str(self, tree):
        if not tree:
            return None
        if not tree.left and not tree.right:
            return f'{self.class_name}({tree.val})'
        if not tree.left:
            return f'{self.class_name}({tree.val}, None, {self._to_str(tree.right)})'
        if not tree.right:
            return f'{self.class_name}({tree.val}, {self._to_str(tree.left)}, None)'
        return f'{self.class_name}({tree.val}, {self._to_str(tree.left)}, {self._to_str(tree.right)})'

    def __repr__(self):
        return self._to_str(self)

    def to_str(self):
        return self._to_str(self)

    def _is_equal(self, a, b):
        if not a and not b:
            return True

        if a and not b:
            return False

        if b and not a:
            return False

        if a.val != b.val:
            return False

        return self._is_equal(a.right, b.right) and self._is_equal(a.left, b.left)

    def __eq__(self, other):
        return self._is_equal(self, other)


def mirror(tree: Optional[TreeNode]) -> Optional[TreeNode]:
    """Return symmetric version of a tree"""
    if not tree:
        return None
    if tree.left and tree.right:
        tree.left, tree.right = mirror(tree.right), mirror(tree.left)
    elif tree.left:
        tree.left, tree.right = tree.right, mirror(tree.left)
    elif tree.right:
        tree.left, tree.right = mirror(tree.right), tree.left
    return tree


def check_symmetric(tree: Optional[TreeNode]) -> bool:
    return tree.left == mirror(tree.right)


if __name__ == '__main__':
    # Test mirror func
    tree = TreeNode(0, TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(4, TreeNode(5), TreeNode(6)))
    assert mirror(tree) == TreeNode(0, TreeNode(4, TreeNode(6), TreeNode(5)), TreeNode(1, TreeNode(3), TreeNode(2)))

    tree = TreeNode(1, TreeNode(2, None, TreeNode(3)))
    assert mirror(tree) == TreeNode(1, None, TreeNode(2, TreeNode(3), None))

    tree = TreeNode(1, TreeNode(2))
    assert mirror(tree) == TreeNode(1, None, TreeNode(2))

    # Test check_symmetric func
    tree = TreeNode(10, TreeNode(5, TreeNode(0), TreeNode(6)), TreeNode(5, TreeNode(0), TreeNode(6)))
    assert check_symmetric(tree) is False

    tree = TreeNode(10, TreeNode(5, TreeNode(6), TreeNode(0)), TreeNode(5, TreeNode(0), TreeNode(6)))
    assert check_symmetric(tree) is True

    tree = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
    assert check_symmetric(tree) is False

    tree = TreeNode(1, TreeNode(2, TreeNode(3), None), TreeNode(2, None, TreeNode(3)))
    assert check_symmetric(tree) is True
