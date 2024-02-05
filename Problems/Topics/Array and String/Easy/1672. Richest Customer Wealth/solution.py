from typing import List


def find_richest_balance(accounts: List[int]) -> int:
    """


    Time complexity: O(n)
    Space complexity: O(1)

    """
    max_balance = 0
    for account in accounts:
        balance = sum(account)
        if balance > max_balance:
            max_balance = balance

    return max_balance


if __name__ == '__main__':
    actual, expected = find_richest_balance(accounts=[[1, 2, 3], [3, 2, 1]]), 6
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_richest_balance(accounts=[[1, 5], [7, 3], [3, 5]]), 10
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_richest_balance(accounts=[[2, 8, 7], [7, 1, 3], [1, 9, 5]]), 17
    assert actual == expected, f"expected: {expected}, actual: {actual}"
