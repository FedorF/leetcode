from typing import List


def generate_seq_numbers(low: int, high: int) -> List[int]:
    """

    Let's take a look at possible sequential numbers varying number of digits.

        n_digits=9: [123456789]
        n_digits=8: [12345678, 23456789]
        n_digits=7: [1234567, 2345678, 3456789]
        ...
        n_digits=1: [12, 23, 34, 45, 56, 67, 78, 89]

    So, the minimum possible sequential number is "12", and maximum possible is "123456789"

    Approach: let's define "base" sequential number and use it for generating other sequential numbers.
    Run through all digit length from len(low) to len(high) and generate all possible sequential numbers using "base"
    number.
    If len(high) is greater than 9, the greatest possible sequential number is 123456789.


    Time complexity: O(1)
    Space complexity: O(1)

    """
    if len(str(low)) > 9:
        return []

    res = []
    base = "123456789"
    for n_digits in range(len(str(low)), min(len(base) + 1, len(str(high)) + 1)):
        for i in range(n_digits, len(base) + 1):
            seq_num = int(base[i - n_digits:i])
            if seq_num > high:
                return res

            if seq_num >= low:
                res.append(seq_num)
    return res


if __name__ == '__main__':
    actual, expected = generate_seq_numbers(low=10, high=100), [12, 23, 34, 45, 56, 67, 78, 89]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = generate_seq_numbers(low=100, high=300), [123, 234]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = generate_seq_numbers(low=1000, high=13000), [1234, 2345, 3456, 4567, 5678, 6789, 12345]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
