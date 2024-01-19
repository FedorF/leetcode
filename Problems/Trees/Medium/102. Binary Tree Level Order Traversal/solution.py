from collections import OrderedDict
from typing import Dict, List, Optional


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_tree_levels(tree: Optional[TreeNode]) -> List[List[int]]:
    def add_level(tree: Optional[TreeNode], levels: Dict[int, List[int]], i: int):
        if i not in levels:
            levels[i] = []
        levels[i].append(tree.val)
        if tree.left:
            add_level(tree.left, levels, i + 1)
        if tree.right:
            add_level(tree.right, levels, i + 1)

    if tree is None:
        return []
    levels = {}
    add_level(tree, levels, 0)
    levels = [x for _, x in sorted(levels.items(), key=lambda x: x[0])]
    return levels


def find_tree_levels(tree: Optional[TreeNode]) -> List[List[int]]:
    def add_level(tree: Optional[TreeNode], levels: Dict[int, List[int]], i: int):
        if i not in levels:
            levels[i] = []

        levels[i].append(tree.val)

        if tree.left:
            add_level(tree.left, levels, i + 1)

        if tree.right:
            add_level(tree.right, levels, i + 1)

    if tree is None:
        return []

    levels = OrderedDict()
    add_level(tree, levels, 0)
    levels = [x for _, x in levels.items()]
    return levels


if __name__ == '__main__':
    assert find_tree_levels(None) == []
    assert find_tree_levels(TreeNode(100)) == [[100]]
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert find_tree_levels(tree) == [[3], [9, 20], [15, 7]]
