from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(xs: List[int]) -> Optional[TreeNode]:
    if not xs:
        return

    def dfs(ind: int = 0) -> TreeNode:
        if ind >= len(xs) or xs[ind] is None:
            return

        node = TreeNode(xs[ind])
        node.left = dfs(2 * ind + 1)
        node.right = dfs(2 * ind + 2)
        return node

    return dfs()


class BSTIterator:
    """
    DFS iterative approach using stack.


    Time complexity: O(1)  (on average)
    Space complexity: O(depth)

    """

    def __init__(self, root: Optional[TreeNode]):
        """
        Initiate stack and add left-most subtree nodes

        """
        self.stack = []
        self.add_node(root)

    def add_node(self, node):
        """
        Adds left-most subtree nodes to stack

        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Extract node from stack and add it's right sub-node to stack

        """
        node = self.stack.pop()
        self.add_node(node.right)
        return node.val

    def has_next(self) -> bool:
        return len(self.stack) > 0


def run_test(commands: List[str], tree: TreeNode):
    tree_iter = BSTIterator(tree)
    res = []
    for command in commands:
        output = getattr(tree_iter, command)()
        res.append(output)

    return res


if __name__ == '__main__':
    commands = ["next", "next", "has_next", "next", "has_next", "next", "has_next", "next", "has_next"]
    tree = build_tree([7, 3, 15, None, None, 9, 20])
    actual, expected = run_test(commands, tree), [3, 7, True, 9, True, 15, True, 20, False]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
