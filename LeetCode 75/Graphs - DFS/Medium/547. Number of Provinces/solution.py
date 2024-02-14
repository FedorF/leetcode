from typing import List


def count_clusters(graph: List[List[int]]) -> int:
    """
    DFS Graph approach.


    Time complexity: O(n^2)
    Space complexity: O(n)

    """

    def dfs(node):
        """
        Travels through all neighbors of current node

        """
        for neighbor in range(n):
            if (neighbor not in seen) and (graph[node][neighbor] == 1):
                seen.add(neighbor)
                dfs(neighbor)
        return

    n = len(graph)
    seen = set()
    cnt = 0
    for i in range(n):  # iterate through all nodes (rows)
        if i not in seen:
            # we've never seen current node, so start new cluster from it
            cnt += 1
            seen.add(i)
            dfs(i)

    return cnt


if __name__ == '__main__':
    actual, expected = count_clusters([[1, 1, 0], [1, 1, 0], [0, 0, 1]]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_clusters([[1, 0, 0], [0, 1, 0], [0, 0, 1]]), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_clusters([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
