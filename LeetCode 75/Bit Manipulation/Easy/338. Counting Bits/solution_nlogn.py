from typing import List


def count_ones_in_binary(n: int) -> List[int]:
    """
    Brute force solution.
    Iterate through all numbers, find binary representation and count ones.

    Complexity is n operations to traverse through all numbers, and log(n) operations on each step for counting ones.
    log(n) - is because we need to make log(n) operations (divisions by 2) to transform decimal number to binary, so
    we'll have log(n) bits in binary representation.


    Time complexity: O(n*log(n))
    Space complexity: O(n)

    """
    res = []
    for decimal in range(n + 1):
        binary = format(decimal, "b")
        ones_cnt = 0
        for bit in binary:
            if bit == "1":
                ones_cnt += 1
        res.append(ones_cnt)

    return res


if __name__ == '__main__':
    actual, expected = count_ones_in_binary(2), [0, 1, 1]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = count_ones_in_binary(5), [0, 1, 1, 2, 1, 2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
