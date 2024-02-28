from typing import List


def sort_courses(n: int, prerequisites: List[List[int]]) -> List[int]:
    """

    Time complexity: O(V+E)
    Space complexity: O(V+E)


    """
    graph = {i: [] for i in range(n)}  # maps course -> prerequisites
    for crs, pre in prerequisites:
        graph[crs].append(pre)

    def dfs(course):
        """
        Returns:
            - False, if there is a cycle in the graph;
            - True, if there is no cycle, and it's possible to build topological order.

        """
        if course in cycle:  # found a cycle in graph
            return False

        if not graph[course]:  # no prerequisites
            if course not in added:
                added.add(course)
                res.append(course)
            return True

        cycle.add(course)
        for pre in graph[course]:  # run dfs from every adjacent node
            if dfs(pre) is False:
                return False

        cycle.remove(course)
        graph[course] = []  # finished all prerequisites, so course is finished too

        if course not in added:
            added.add(course)
            res.append(course)

        return True

    cycle = set()  # keeps track on nodes to find a cycle
    added = set()  # keeps track on nodes that are already added to resulting list
    res = []
    for i in range(n):  # start dfs from every node
        if not dfs(i):
            return []

    return res


if __name__ == '__main__':
    actual, expected = sort_courses(2, [[1, 0]]), [0, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = sort_courses(4, [[1, 0], [2, 0], [3, 1], [3, 2]]), [0, 1, 2, 3]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = sort_courses(1, []), [0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
