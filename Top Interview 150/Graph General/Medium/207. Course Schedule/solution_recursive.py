from typing import List


def can_finish_courses(n: int, prerequisites: List[List[int]]) -> bool:
    """
    This problem is equivalent to finding if a cycle exists in a directed graph.
    If a cycle exists, no topological ordering exists, and therefore it will be impossible to take all courses.


    Time complexity: O(V+E)
    Space complexity: O(V+E)

    """
    if not prerequisites:
        return True

    graph = {i: [] for i in range(n)}  # maps course -> prerequisites
    for crs, pre in prerequisites:
        graph[crs].append(pre)

    def dfs(course: int):
        """
        Returns:
            - False, if there is a cycle in the graph;
            - True, if there is no cycle, and it's possible to build topological order.

        """
        if course in cycle:  # found a cycle in graph
            return False

        if not graph[course]:  # no prerequisites
            return True

        cycle.add(course)
        for pre in graph[course]:  # run dfs from every adjacent node
            if dfs(pre) is False:
                return False

        cycle.remove(course)
        graph[course] = []  # finished all prerequisites, so course is finished too
        return True

    cycle = set()
    for i in range(n):  # start dfs from every node
        if dfs(i) is False:
            return False

    return True


if __name__ == '__main__':
    prerequisites = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
    actual, expected = can_finish_courses(20, prerequisites), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_finish_courses(2, []), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_finish_courses(2, [[1, 0]]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_finish_courses(2, [[1, 0], [0, 1]]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_finish_courses(3, [[1, 0], [1, 2], [0, 1]]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
