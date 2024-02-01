from typing import List


def calc_days_to_warmer_temp(temperatures: List[int]) -> List[int]:
    """
    Stack approach.
    Define resulting list and fill it with zeros.
    Define stack and run through all days. Put a pair of (temp, index) in the stack.
    Compare last temperature value in stack with current day. If it's greater, pop element from
    stack, and add difference between current day's index and index from stack to resulting list.

    (See illustration in Readme.md)


    Time complexity: O(n)
    Space complexity: O(n)

    """
    res = [0] * len(temperatures)
    stack = []
    i = 0
    while i < len(temperatures):  # run through all days
        # current day's temperature is greater
        if stack and (stack[-1][0] < temperatures[i]):
            _, ind = stack.pop()  # so pop last element from stack
            res[ind] = i - ind  # and add difference between indexes to resulting list
        else:
            stack.append((temperatures[i], i))  # add a pair of (temp, ind) to stack
            i += 1  # consider next day

    return res


if __name__ == '__main__':
    actual, expected = calc_days_to_warmer_temp([73, 74, 75, 71, 69, 72, 76, 73]), [1, 1, 4, 2, 1, 1, 0, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_days_to_warmer_temp([75]), [0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_days_to_warmer_temp([75, 71]), [0, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_days_to_warmer_temp([75, 76]), [1, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_days_to_warmer_temp(temperatures=[30, 40, 50, 60]), [1, 1, 1, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_days_to_warmer_temp(temperatures=[30, 60, 90]), [1, 1, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
