from typing import List


def find_min_coins_change(coins: List[int], amount: int) -> int:
    """
    DP (bottom-up) approach.
    Start at amount = 0.

    1) How many ways to combine coins to 0? It's 0.
    dp[0] = 0

    2) How many ways to combine coins to get 1?
    dp[1] = 1 (if we have $1 coin)

    3) How many ways to combine coins to get 2?
    dp[2] = 1 + dp[2-1] (if we have $1 coin),
     or
    dp[2] = 1 (if we have $2 coin)

    So, at each step we should iterate through all the coins and find min coins needed to combine current amount.
    And we should iterate through all possible amounts from 0 to target.

    Time complexity: O(len(coins) * amount)
    Space complexity: O(amount)

    """
    dp = [amount + 1] * (amount + 1)  # define dp list and fill it with some "big" value, e.g. amount + 1
    dp[0] = 0  # base case
    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])

    if dp[amount] != amount + 1:
        return dp[amount]

    return -1


if __name__ == '__main__':
    assert find_min_coins_change(coins=[1, 2, 5, 50], amount=11) == 3
    assert find_min_coins_change(coins=[1, 2, 5], amount=11) == 3
    assert find_min_coins_change(coins=[2], amount=3) == -1
    assert find_min_coins_change(coins=[1], amount=0) == 0
    assert find_min_coins_change(coins=[186, 419, 83, 408], amount=6249) == 20
