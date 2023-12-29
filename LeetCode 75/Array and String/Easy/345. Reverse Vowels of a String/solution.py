def reverse_vowels(s: str) -> str:
    """
    Use two pointers and swap letters if they are both vowels.


    Time complexity: O(n)
    Space complexity: O(n)

    """
    vowels = set("AaEeIiOoUu")
    res = list(s)
    left, right = 0, len(res) - 1
    while left < right:
        if (res[left] in vowels) and (res[right] in vowels):
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1
            continue

        if (res[left] in vowels) and (res[right] not in vowels):
            right -= 1
            continue

        if (res[left] not in vowels) and (res[right] in vowels):
            left += 1
            continue

        left += 1
        right -= 1

    return "".join(res)


if __name__ == '__main__':
    actual, expected = reverse_vowels(s="hello"), "holle"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = reverse_vowels(s="leetcode"), "leotcede"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = reverse_vowels(s="x"), "x"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = reverse_vowels(s="a"), "a"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = reverse_vowels(s="aeo"), "oea"
    assert actual == expected, f"expected: {expected}, actual: {actual}"
