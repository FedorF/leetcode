from typing import List


def max_points_on_line(points: List[List[int]]) -> int:
    """


    Time complexity: O()
    Space complexity: O()

    """
    pass


if __name__ == '__main__':
    actual, expected = max_points_on_line(points=[[1, 1], [2, 2], [3, 3]]), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = max_points_on_line(points=[[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"
