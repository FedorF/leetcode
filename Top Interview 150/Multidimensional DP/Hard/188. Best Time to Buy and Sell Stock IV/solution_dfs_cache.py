from typing import List


def calc_max_profit(k: int, prices: List[int]) -> int:
    """

    Raises "Memory Limit Exceeded"
    """
    cache = {}

    def trade(buy_day: int = -1, day: int = 0, transact_cnt: int = k, balance: int = 0) -> int:
        key = (day, balance, buy_day)

        if transact_cnt == 0:
            return balance

        if day == len(prices) - 1:  # last date
            if buy_day < 0:
                return balance
            return balance + max(0, prices[day] - prices[buy_day])

        if key in cache:
            return cache[key]

        if buy_day >= 0:  # we have a stock, so we can sell it
            if prices[day] - prices[buy_day] <= 0:  # not profitable
                profit = trade(buy_day, day + 1, transact_cnt, balance)  # keep
            else:
                profit = max(
                    trade(-1, day + 1, transact_cnt - 1, balance + prices[day] - prices[buy_day]),  # sell
                    trade(buy_day, day + 1, transact_cnt, balance)  # keep
                )
        else:  # we don't have a stock, so we can buy it
            profit = max(
                trade(day, day + 1, transact_cnt, balance),  # buy
                trade(-1, day + 1, transact_cnt, balance)  # buy later
            )

        cache[key] = profit
        return cache[key]

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
