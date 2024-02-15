from typing import List


def count_ones_in_binary(n: int) -> List[int]:
    """
    There are two facts:
    1) Since multiplying by 2 just adds a zero to the end,
    then any number and its double will have the same number of 1's.
    2) Likewise, doubling a number and adding one will increase the count by exactly 1.

    Or, in other words:
        countBits(N) = countBits(2N)
        countBits(N)+1 = countBits(2N+1)

    Thus, we can see that any number will have the same bit count as half that number,
    with an extra one if it's an odd number.

    We iterate through the range of numbers and calculate each bit count successively in this manner:
        for i in range(num):
            counter[i] = counter[i // 2] + i % 2

    But instead dividing by 2, we can use right-shift operation for efficiency.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    res = [0] * (n + 1)
    for i in range(1, n + 1):
        res[i] = res[i >> 1] + i % 2

    return res


if __name__ == '__main__':
    actual, expected = count_ones_in_binary(2), [0, 1, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_ones_in_binary(5), [0, 1, 1, 2, 1, 2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
