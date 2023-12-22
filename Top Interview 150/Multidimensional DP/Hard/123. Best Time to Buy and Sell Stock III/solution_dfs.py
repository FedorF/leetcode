from typing import List


def calc_max_profit(prices: List[int]) -> int:
    cache = {}

    def trade(has_stock: bool = False, day: int = 0, transact_cnt: int = 2) -> int:
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
    actual, expected = calc_max_profit(prices=[3, 3, 5, 0, 0, 3, 1, 4]), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(prices=[1, 2, 3, 4, 5]), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(prices=[7, 6, 4, 3, 1]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(prices=[3, 2, 6, 5, 0, 3]), 7
    assert actual == expected, f"expected: {expected}, actual: {actual}"
