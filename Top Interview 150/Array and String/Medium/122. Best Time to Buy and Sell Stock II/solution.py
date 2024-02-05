from typing import List


def calc_max_profit(prices: List[int]) -> int:
    """

    Time complexity: O(n)
    Space complexity: O(1)

    """
    profit = 0
    for i in range(len(prices) - 1):
        profit += max(0, prices[i + 1] - prices[i])
    return profit


if __name__ == '__main__':
    assert calc_max_profit([7, 6, 4, 3, 1]) == 0
    assert calc_max_profit([1, 2, 3, 4, 5]) == 4
    assert calc_max_profit([7, 1, 5, 3, 6, 4]) == 7
    assert calc_max_profit([10]) == 0
