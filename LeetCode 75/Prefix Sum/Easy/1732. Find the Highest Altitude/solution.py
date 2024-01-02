from typing import List


def find_max_altitude(gain: List[int]) -> int:
    """
    Calculate cumulative sum and find max element.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    max_altitude = cur_altitude = 0
    for x in gain:
        cur_altitude += x
        max_altitude = max(max_altitude, cur_altitude)
    return max_altitude


if __name__ == '__main__':
    actual, expected = find_max_altitude([-5, 1, 5, 0, -7]), 1
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_max_altitude([-4, -3, -2, -1, 4, 3, 2]), 0
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_max_altitude([10]), 10
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = find_max_altitude([-10]), 0
    assert actual == expected, f"actual: {actual}, expected: {expected}"
