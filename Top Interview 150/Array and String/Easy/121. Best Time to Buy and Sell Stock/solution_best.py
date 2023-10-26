from typing import List


def calc_max_profit(prices: List[int]) -> int:
    """
    Linear time and constant space.
    We can keep track of minimal buying price and maximal profit we could reach at each timestamp.
    """
    buy_min = prices[0]
    profit_max = 0
    for i in range(1, len(prices)):
        profit_max = max(profit_max, prices[i]-buy_min)
        buy_min = min(buy_min, prices[i])
    return profit_max


if __name__ == '__main__':
    prices = [7,6,4,3,1]
    assert calc_max_profit(prices) == 0

    prices = [7,1,5,3,6,4]
    assert calc_max_profit(prices) == 5

    prices = [100]
    assert calc_max_profit(prices) == 0
