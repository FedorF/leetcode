def calc_gcd(x: int, y: int) -> int:
    """
    Euclidean algorithm (https://en.wikipedia.org/wiki/Greatest_common_divisor)

    Time complexity: O(log(x * y))
    Space complexity: O(1)

    """
    if x == 0:
        return y

    if y == 0:
        return x

    if x >= y:
        return calc_gcd(y, x % y)

    return calc_gcd(x, y % x)


def find_greatest_common_divisor(x: str, y: str) -> str:
    """
    Tricky approach: strings have GCD if and only if s1 + s2 == s2 + s1

    Time complexity: O(len(x) + len(y))
    Space complexity: O(1)

    """
    if x + y == y + x:  # check if there is a GCD
        return x[:calc_gcd(len(x), len(y))]  # we can use math.gcd() instead

    return ""


if __name__ == '__main__':
    actual, expected = find_greatest_common_divisor("ABCABC", "ABC"), "ABC"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_greatest_common_divisor("ABABAB", "ABAB"), "AB"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_greatest_common_divisor("LEET", "CODE"), ""
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_greatest_common_divisor("abcd", "abc"), ""
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = find_greatest_common_divisor("aaaaa", "aa"), "a"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    x = "TAUXXTAUXXTAUXXTAUXXTAUXX"
    y = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
    actual, expected = find_greatest_common_divisor(x=x, y=y), "TAUXX"
    assert actual == expected, f"expected: {expected}, actual: {actual}"
