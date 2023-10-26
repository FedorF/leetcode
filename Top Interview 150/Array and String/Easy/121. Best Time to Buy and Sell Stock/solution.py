from typing import List


def calc_max_profit(prices: List[int]) -> int:
    """
    Brute Force solution. Squared time complexity.
    """
    profit = 0
    for buy in range(len(prices)-1):
        for sell in range(buy+1, len(prices)):
            profit = max(profit, prices[sell] - prices[buy])
    return profit


if __name__ == '__main__':
    prices = [7,6,4,3,1]
    assert calc_max_profit(prices) == 0

    prices = [7,1,5,3,6,4]
    assert calc_max_profit(prices) == 5

    prices = [100]
    assert calc_max_profit(prices) == 0




