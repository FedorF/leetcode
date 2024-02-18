from typing import List


def plus_one(digits: List[int]) -> List[int]:
    """

    1. Run backward
      E.g., [9,9,9] -> [0,0,0], carry=1

    2. Inplace carry into first position and shift every value to the right
      [0,0,0], carry=1 -> [1,0,0], carry=0

    3. Add last value to the list
      [1,0,0], carry=0 -> [1,0,0,0]

    Time complexity: O(n)
    Space complexity: O(1)

    """
    digits[-1] += 1

    carry = 0
    for i in range(len(digits) - 1, -1, -1):  # run backward and update values with respect to carry
        digits[i] += carry
        digits[i], carry = digits[i] % 10, digits[i] // 10
        if carry == 0:
            return digits

    # carry doesn't equal to zero, so inplace carry into first position, and shift every value to the right
    for i in range(len(digits)):
        digits[i], carry = carry, digits[i]

    # add last value to the list
    digits.append(carry)
    return digits


if __name__ == '__main__':
    actual, expected = plus_one([1, 2, 3]), [1, 2, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = plus_one([9]), [1, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = plus_one([1, 9, 9]), [2, 0, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = plus_one([9, 9, 9]), [1, 0, 0, 0]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
