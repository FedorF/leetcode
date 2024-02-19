from collections import defaultdict
from typing import List


def max_points_on_line(points: List[List[int]]) -> int:
    """
    Line equation: y = k*x + b
    We can store all points that lie on the same line using a key: (k, b)


    Time complexity: O(n^2)
    Space complexity: O(n^2)

    """
    if len(points) == 1:
        return 1

    max_points = 0
    lines = defaultdict(set)
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            if x1 == x2:
                k, b = None, x1
            else:
                k = (y1 - y2) / (x1 - x2)
                b = (x1 * y2 - x2 * y1) / (x1 - x2)

            lines[(k, b)].add(i)
            lines[(k, b)].add(j)
            max_points = max(max_points, len(lines[(k, b)]))

    return max_points


if __name__ == '__main__':
    actual, expected = max_points_on_line(points=[[0, 0]]), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = max_points_on_line(points=[[1, 1], [2, 2], [3, 3]]), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = max_points_on_line(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"
