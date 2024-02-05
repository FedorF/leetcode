from typing import Optional


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def check_bst(root: Optional[TreeNode]) -> bool:
    def check_(
            tree: Optional[TreeNode],
            _min: Optional[int] = None,
            _max: Optional[int] = None,
    ) -> bool:
        if not tree:
            return False
        if tree.left:
            if tree.left.val >= tree.val:
                return False
            if _min and (tree.left.val <= _min):
                return False
            if not check_(tree.left, _min, tree.val):
                return False

        if tree.right:
            if tree.right.val <= tree.val:
                return False
            if _max and (tree.right.val >= _max):
                return False
            if not check_(tree.right, tree.val, _max):
                return False
        return True

    return check_(root)


if __name__ == '__main__':
    assert check_bst(None) is False

    tree = TreeNode(10, left=None, right=None)
    assert check_bst(tree) is True

    tree = TreeNode(10, None, TreeNode(10))
    assert check_bst(tree) is False

    tree = TreeNode(2, TreeNode(1), TreeNode(3))
    assert check_bst(tree) is True

    tree = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert check_bst(tree) is False

    tree = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    assert check_bst(tree) is False
