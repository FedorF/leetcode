def find_gcd(long: str, short: str) -> str:
    """
    Iterate through all elements of short string and if we can build string with lengths of both strings, check if
    built strings are equal to input ones.


    Time complexity: O(short * (len(long) + len(short)))
    Space complexity: O(len(short))

    """
    res = div = ""
    for i in range(len(short)):
        div += short[i]  # update divider
        # check if it's possible to build strings using current divider
        if (len(long) % len(div) == 0) and (len(short) % len(div) == 0):
            if long == div * (len(long) // len(div)) and short == div * (len(short) // len(div)):
                res = div  # if it's possible, update result variable
    return res


def find_greatest_common_divisor(x: str, y: str) -> str:
    """
    Time complexity: O(min(len(x), len(y)) * (len(x) + len(y)))
    Space complexity: O(len(min(x, y)))

    """
    if x == y:
        return x

    if len(x) < len(y):  # find the shortest input string and start search
        return find_gcd(long=y, short=x)

    return find_gcd(long=x, short=y)


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
