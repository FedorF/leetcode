from typing import List


def calc_min_cost(cost: List[int]) -> int:
    """
    Dynamical Programming approach.
    In-place update input list with the minimum cost to reach current step.


    Time complexity: O(n)
    Space complexity: O(1)  (due to in-place transformation of input list)

    """
    cost.append(0)  # add goal step
    for i in range(2, len(cost)):
        cost[i] += min(cost[i - 1], cost[i - 2])

    return cost[-1]


if __name__ == '__main__':
    actual, expected = calc_min_cost(cost=[10, 15, 20]), 15
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_cost(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_cost(cost=[0, 100]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_cost(cost=[100, 0]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
