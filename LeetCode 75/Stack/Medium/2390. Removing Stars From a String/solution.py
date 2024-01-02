def remove_asterisks(s: str) -> str:
    """
    Use stack: pop element if it's an asterisk and append if it's something else.

    Time complexity: O(n)
    Space complexity: O(n)

    """
    stack = []
    for ch in s:
        if ch == "*":
            stack.pop()
        else:
            stack.append(ch)

    return "".join(stack)


if __name__ == '__main__':
    actual, expected = remove_asterisks("leet**cod*e"), "lecoe"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = remove_asterisks("erase*****"), ""
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = remove_asterisks("a*"), ""
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = remove_asterisks("a*a"), "a"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = remove_asterisks("aa*"), "a"
    assert actual == expected, f"expected: {expected}, actual: {actual}"
