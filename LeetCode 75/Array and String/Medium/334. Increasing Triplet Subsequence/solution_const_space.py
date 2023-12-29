import math
from typing import List


def exists_increasing_triplet(nums: List[int]) -> bool:
    """
    One pass approach. We keep 2 numbers first and second where first < second, and first number must be before second
    number.
    Iterate through elements:
    - If num <= first then update the first as minimum as possible, by first = num
    - Else If num <= second then update second as minimum as possible (since now first < num <= second), by second = num
    - Else, now first < second < num then we found a valid Increasing Triplet Subsequence, return True.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    first = second = math.inf
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:  # now first < num, if num <= second then try to make second as small as possible
            second = num
        else:  # now first < second < num
            return True

    return False


if __name__ == '__main__':
    actual, expected = exists_increasing_triplet(nums=[6, 7, 1, 2]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[1, 2, 3, 4, 5]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[5, 4, 3, 2, 1]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[2, 1, 5, 0, 4, 6]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[2, 1, 5]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[1, 2, 3]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = exists_increasing_triplet(nums=[1, 2]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
