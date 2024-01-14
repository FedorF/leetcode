from typing import List


def calc_min_cost(cost: List[int]) -> int:
    """
    Dynamical Programming approach.
    Use two pointers to keep track on cost.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    first, second = cost[0], cost[1]
    for i in range(2, len(cost)):
        first, second = second, cost[i] + min(first, second)

    return min(first, second)


if __name__ == '__main__':
    actual, expected = calc_min_cost(cost=[10, 15, 20]), 15
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_cost(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_cost(cost=[0, 100]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_cost(cost=[100, 0]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
