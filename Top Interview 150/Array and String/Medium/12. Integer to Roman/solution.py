def int_to_roman(num: int) -> str:
    """

    Time complexity: O(1)
    Space complexity: O(1)

    """
    translate = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I',
    }
    res = ""
    for base, roman in translate.items():
        if num == 0:
            break

        res += num // base * roman
        num %= base

    return res


if __name__ == '__main__':
    actual, expected = int_to_roman(20), "XX"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = int_to_roman(3), "III"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = int_to_roman(58), "LVIII"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = int_to_roman(1994), "MCMXCIV"
    assert actual == expected, f"expected: {expected}, actual: {actual}"
