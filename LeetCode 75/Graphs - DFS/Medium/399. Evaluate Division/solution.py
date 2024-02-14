from collections import defaultdict
from typing import List


def calc(equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """
    Represent given data as a graph: variables from equations as nodes and values as edges' weights.


    Time complexity: O(len(queries) * E)
    Space complexity: O(V^2)

    """

    def dfs(x: str, y: str):
        """
        DFS Graph function for finding connection (weight) between starting node "x" and target node "y"

        """
        nonlocal seen
        if y in graph[x]:
            return graph[x][y]

        for neighbor in graph[x]:  # run through all neighboring nodes of current x
            if neighbor not in seen:
                seen.add(neighbor)
                weight = dfs(neighbor, y)  # try to reach y starting from current neighbor
                if weight:  # success
                    weight *= graph[x][neighbor]  # calculate product

                    # cache connection
                    graph[x][y] = weight
                    graph[y][x] = 1 / weight
                    return weight
        return

    graph = defaultdict(dict)  # define graph as a dict of dicts
    for i in range(len(equations)):
        x, y = equations[i]  # obtain variables
        graph[x][y] = values[i]  # save weight to go from x to y
        graph[y][x] = 1 / values[i]  # save weight to go from y to x

    res = []
    for x, y in queries:  # run through all queries
        if x not in graph or y not in graph:  # no such variable in graph
            res.append(-1)

        elif x == y:
            res.append(1)

        elif x in graph and y in graph[x]:  # adjacent nodes
            res.append(graph[x][y])

        else:  # restore connection (weight) between nodes
            seen = set()
            val = dfs(x, y) or -1
            res.append(val)

    return res


if __name__ == '__main__':
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    actual = calc(equations, values, queries)
    expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
    actual = calc(equations, values, queries)
    expected = [3.75000, 0.40000, 5.00000, 0.20000]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    actual = calc(equations, values, queries)
    expected = [0.50000, 2.00000, -1.00000, -1.00000]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
