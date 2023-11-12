def check_palindrome(s: str) -> bool:
    """
    One pointer approach.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    s = [x for x in s.lower() if x.isalnum()]
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            return False
    return True


if __name__ == '__main__':
    assert check_palindrome("race a car") is False
    assert check_palindrome("A man, a plan, a canal: Panama") is True
    assert check_palindrome(" ") is True
