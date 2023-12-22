from typing import List


def calc_max_profit(k: int, prices: List[int]) -> int:
    if k >= len(prices) // 2:
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))

    ans = [0] * len(prices)
    for _ in range(k):
        most = 0
        for i in range(1, len(prices)):
            most = max(ans[i], most + prices[i] - prices[i - 1])
            ans[i] = max(ans[i - 1], most)
    return ans[-1]


if __name__ == '__main__':
    actual, expected = calc_max_profit(k=4, prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0]), 15
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=2, prices=[2, 4, 1]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=10, prices=[100]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=2, prices=[3, 2, 6, 5, 0, 3]), 7
    assert actual == expected, f"expected: {expected}, actual: {actual}"
