def check_palindrome(s: str) -> bool:
    """
    Time complexity: O(n) + O(n) + O(n)
    Space complexity: O(n)
    """
    s = ''.join(filter(lambda x: x.isalnum(), s.lower()))
    return s == s[::-1]


if __name__ == '__main__':
    assert check_palindrome("race a car") is False
    assert check_palindrome("A man, a plan, a canal: Panama") is True
    assert check_palindrome(" ") is True
