from typing import List


def calc_max_profit(k: int, prices: List[int]) -> int:
    if k == 0:  # no transactions available
        return 0

    if k >= len(prices) // 2:  # we can make as many transactions as we want to
        profit = 0
        for i in range(1, len(prices)):
            profit += max(0, prices[i] - prices[i - 1])
        return profit

    cache = {}

    def trade(has_stock: bool = False, day: int = 0, transact_cnt: int = k) -> int:
        if transact_cnt == 0 or day >= len(prices):
            return 0

        sell = buy = 0
        if has_stock:
            sell = prices[day] + trade(has_stock=False, day=day + 1, transact_cnt=transact_cnt - 1)
        else:
            buy = -prices[day] + trade(has_stock=True, day=day + 1, transact_cnt=transact_cnt)
        keep = trade(has_stock=has_stock, day=day + 1, transact_cnt=transact_cnt)

        cache[(has_stock, day, transact_cnt)] = max(sell, buy, keep)
        return cache[(has_stock, day, transact_cnt)]

    return trade()


if __name__ == '__main__':
    actual, expected = calc_max_profit(k=4, prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0]), 15
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=2, prices=[2, 4, 1]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=10, prices=[100]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=2, prices=[3, 2, 6, 5, 0, 3]), 7
    assert actual == expected, f"expected: {expected}, actual: {actual}"
