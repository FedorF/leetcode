from typing import List


def find_peak_element_index(xs: List[int]) -> int:
    """
    Linear approach. Run through elements and compare element with adjacent ones.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    if len(xs) == 1:
        return 0

    for i in range(len(xs)):
        if i == 0:
            if xs[i] > xs[i + 1]:
                return i

        if i == len(xs) - 1:
            if xs[i] > xs[i - 1]:
                return i

        if xs[i - 1] < xs[i] > xs[i + 1]:
            return i


if __name__ == '__main__':
    actual, expected = find_peak_element_index([1, 2, 3, 1]), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_peak_element_index([1, 2, 1, 3, 5, 6, 4]), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_peak_element_index([1]), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"
