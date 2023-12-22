from typing import List


def calc_max_profit(k: int, prices: List[int]) -> int:
    # no transaction, no profit
    if k == 0:
        return 0
    # dp[k][0] = min cost you need to spend at most k transactions
    # dp[k][1] = max profit you can achieve at most k transactions
    dp = [[1000, 0] for _ in range(k + 1)]
    for price in prices:
        for i in range(1, k + 1):
            # price - dp[i - 1][1] is how much you need to spend
            # i.e. use the profit you earned from previous transaction to buy the stock
            # we want to minimize it
            dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
            # price - dp[i][0] is how much you can achieve from previous min cost
            # we want to maximize it
            dp[i][1] = max(dp[i][1], price - dp[i][0])
    # return max profit at most k transactions,
    # or you can write `return dp[-1][1]`
    return dp[k][1]


if __name__ == '__main__':
    actual, expected = calc_max_profit(k=4, prices=[1, 2, 4, 2, 5, 7, 2, 4, 9, 0]), 15
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=2, prices=[2, 4, 1]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=10, prices=[100]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_max_profit(k=2, prices=[3, 2, 6, 5, 0, 3]), 7
    assert actual == expected, f"expected: {expected}, actual: {actual}"
