from typing import List


def max_points_on_line(points: List[List[int]]) -> int:
    """
    Line equation: y = k*x + b
    We can store all points that lie on the same line using only slope "k" as a key.
    

    Time complexity: O(n^2)
    Space complexity: O(n)

    """
    if len(points) == 1:
        return 1

    max_points = 0
    for i in range(len(points) - 1):
        x1, y1 = points[i]
        lines = {}  # reset the lines dict for current point
        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            k = (y1 - y2) / (x1 - x2) if x1 != x2 else None

            if k in lines:
                lines[k] += 1
            else:
                lines[k] = 2

            max_points = max(max_points, lines[k])

    return max_points


if __name__ == '__main__':
    actual, expected = max_points_on_line(points=[[0, 0]]), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = max_points_on_line(points=[[1, 1], [2, 2], [3, 3]]), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = max_points_on_line(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"
