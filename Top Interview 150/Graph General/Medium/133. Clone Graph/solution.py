from typing import List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def copy_graph(graph: Optional[Node]) -> Optional[Node]:
    """
    DFS Graph approach.


    Time complexity: O(n_nodes)
    Space complexity: O(n_nodes)

    """
    seen = {}

    def dfs(node: Optional[Node]):
        if node is None:
            return

        node_copy = Node(node.val)
        seen[node.val] = node_copy  # all values are unique in the graph

        neighbors = []
        for neighbor in node.neighbors:
            if neighbor.val not in seen:
                neighbors.append(dfs(neighbor))
            else:
                neighbors.append(seen[neighbor.val])

        node_copy.neighbors = neighbors
        return node_copy

    return dfs(graph)
