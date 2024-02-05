from typing import List, Optional


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


def build_bts(nums: List[int]) -> Optional[TreeNode]:
    def build_node(nums: List[int]) -> Optional[TreeNode]:
        len_ = len(nums)
        if len_ == 0:
            return None

        left_node = build_node(nums[:len_ // 2])
        right_node = build_node(nums[len_ // 2 + 1:])
        return TreeNode(nums[len_ // 2], left_node, right_node)

    return build_node(nums)


if __name__ == '__main__':
    assert build_bts([]) is None

    tree = build_bts([-10, -3, 0, 5, 9])
    assert tree.to_str() == 'TreeNode(0, TreeNode(-3, TreeNode(-10), None), TreeNode(9, TreeNode(5), None))'

    tree = build_bts([1, 2])
    assert tree.to_str() == 'TreeNode(2, TreeNode(1), None)'

    tree = build_bts([1])
    assert tree.to_str() == 'TreeNode(1)'
