from typing import List


def calc_cum_sum(xs: List[int]) -> List[int]:
    """


    Time complexity: O(n)
    Space complexity: O(1)

    """
    for i in range(1, len(xs)):
        xs[i] += xs[i-1]

    return xs


if __name__ == '__main__':
    actual, expected = calc_cum_sum([1, 2, 3, 4]), [1, 3, 6, 10]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_cum_sum([1, 1, 1, 1, 1]), [1, 2, 3, 4, 5]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_cum_sum([3, 1, 2, 10, 1]), [3, 4, 6, 16, 17]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
