class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_lowest_common_parent(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """

    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """

    def find_lca(node: TreeNode = root):
        # found one of the nodes we are looking for
        # or reached the end of a branch of the binary tree without finding either p or q
        if node is None or node == p or node == q:
            return node

        left = find_lca(node.left)
        right = find_lca(node.right)

        # found both p and q in different subtrees of the current node, and therefore the current node is the lca
        if left and right:
            return node

        # when one of subtrees is None, it means that the other node is not in the subtree of the current root
        # so, return the node that is in the subtree
        if left:
            return left

        if right:
            return right

    return find_lca()
