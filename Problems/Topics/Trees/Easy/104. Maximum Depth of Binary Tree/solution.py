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


def calc_tree_depth(tree: Optional[TreeNode]) -> int:
    def dfs(tree: Optional[TreeNode], depth: int) -> int:
        if not tree:
            return 0

        if tree.left and tree.right:
            max_depth = max(dfs(tree.left, depth), dfs(tree.right, depth))
            return max_depth + 1

        if tree.left:
            return dfs(tree.left, depth) + 1

        if tree.right:
            return dfs(tree.right, depth) + 1

        return depth + 1

    return dfs(tree, 0)


if __name__ == '__main__':
    assert calc_tree_depth(None) == 0

    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert calc_tree_depth(tree) == 3

    tree = TreeNode(1, None, TreeNode(2))
    assert calc_tree_depth(tree) == 2

    tree = TreeNode(left=None, right=None)
    assert calc_tree_depth(tree) == 1
