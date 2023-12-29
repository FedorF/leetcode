from typing import List


def check_if_greater(candies: List[int], margin: int) -> List[bool]:
    """
    Find max number of candies. Iterate through list and check if current plus margin is greater than max.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    max_candies = max(candies)
    res = []
    for i in range(len(candies)):
        res[i] = (candies[i] + margin >= max_candies)
    return res


if __name__ == '__main__':
    actual, expected = check_if_greater(candies=[2, 3, 5, 1, 3], margin=3), [True, True, True, False, True]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = check_if_greater(candies=[4, 2, 1, 1, 2], margin=1), [True, False, False, False, False]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = check_if_greater(candies=[12, 1, 12], margin=10), [True, False, True]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
