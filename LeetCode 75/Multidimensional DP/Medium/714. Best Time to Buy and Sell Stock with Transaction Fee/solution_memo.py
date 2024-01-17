from typing import List


def calc_max_profit(prices: List[int], fee: int) -> int:
    """
    Memoization (caching) approach.


    Time complexity: O()
    Space complexity: O(n)

    """
    cache = {}

    def trade(day: int = 0, has_stock: bool = False) -> int:
        if day >= len(prices):
            return 0

        key = (day, has_stock)
        if key in cache:
            return cache[key]

        buy = sell = 0
        if has_stock:
            sell = prices[day] - fee + trade(day + 1, False)
        else:
            buy = -prices[day] + trade(day + 1, True)

        keep = trade(day + 1, has_stock)
        cache[key] = max(sell, buy, keep)
        return cache[key]

    return trade()


if __name__ == '__main__':
    actual, expected = calc_max_profit(prices=[1, 3, 2, 8, 4, 9], fee=2), 8
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(prices=[1, 3, 7, 5, 10, 3], fee=3), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit([1], 1), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit([1], 0), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit([1, 2], 0), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit([1, 2], 1), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit([1, 2], 100), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
