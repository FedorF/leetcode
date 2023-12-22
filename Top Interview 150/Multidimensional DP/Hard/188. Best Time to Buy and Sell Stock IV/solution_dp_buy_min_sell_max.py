import math
from typing import List


def calc_max_profit(k: int, prices: List[int]) -> int:
    if k >= len(prices) // 2:
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))
    buy, sell = [math.inf] * k, [0] * k
    for x in prices:
        for i in range(k):
            if i:
                buy[i] = min(buy[i], x - sell[i - 1])
            else:
                buy[i] = min(buy[i], x)
            sell[i] = max(sell[i], x - buy[i])
    return sell[-1] if k and prices else 0


if __name__ == '__main__':
    actual, expected = calc_max_profit(k=4, prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0]), 15
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=2, prices=[2, 4, 1]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=10, prices=[100]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=2, prices=[3, 2, 6, 5, 0, 3]), 7
    assert actual == expected, f"expected: {expected}, actual: {actual}"
