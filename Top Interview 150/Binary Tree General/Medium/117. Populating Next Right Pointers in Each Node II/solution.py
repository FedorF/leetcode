from collections import deque


class Node:
    def __init__(
            self,
            val: int = 0,
            left: 'Node' = None,
            right: 'Node' = None,
            next_node: 'Node' = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next_node


def connect(root: Node) -> Node:
    """
    BFS solution.

    Time complexity: O(n_nodes)
    Space complexity: O(1)

    """
    if not root:
        return None

    queue = deque([root])
    while queue:
        prev = None
        for i in range(len(queue)):  # connect current level
            node = queue.popleft()
            node.next_node = prev
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
            prev = node

    return root
