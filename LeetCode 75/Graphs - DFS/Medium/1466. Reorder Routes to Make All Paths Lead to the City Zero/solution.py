from collections import defaultdict
from typing import List


def count_reorders(n: int, connections: List[List[int]]) -> int:
    """
    DFS Graph approach.
    For each city store its neighboring city and "cost".
    "Cost" is equal to zero if route is directed to city, and equals to 1 if route is opposite.
    Iterate through all cities starting with "0" and start routes from each city.

    Time complexity: O(n)
    Space complexity: O(n)

    """

    def dfs(node):
        nonlocal res
        # iterate through all neighboring cities and calculate cost
        for neighbor, cost in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                res += cost
                dfs(neighbor)  # start route from the neighbor
        return

    graph = defaultdict(list)
    for a, b in connections:  # fill graph
        graph[a].append((b, 1))  # cost is equal to 1, if route goes out of city
        graph[b].append((a, 0))  # cost is equal to 0, if route goes to city

    res = 0
    seen = set()
    for i in range(n):  # iterate through all cities
        if i not in seen:
            seen.add(i)
            dfs(i)  # start route from current city

    return res


if __name__ == '__main__':
    actual, expected = count_reorders(6, [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_reorders(5, [[1, 0], [1, 2], [3, 2], [3, 4]]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_reorders(3, [[1, 0], [2, 0]]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
