def check_palindrome(s: str) -> bool:
    """
    Two pointers approach.

    Time complexity: O(n)
    Space complexity: O(1)

    """
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left].isalnum() and s[right].isalnum():
            if s[left].lower() != s[right].lower():
                return False

        elif s[left].isalnum() and not s[right].isalnum():
            right -= 1
            continue

        elif not s[left].isalnum() and s[right].isalnum():
            left += 1
            continue

        left += 1
        right -= 1

    return True


if __name__ == '__main__':
    assert check_palindrome("race a car") is False
    assert check_palindrome("A man, a plan, a canal: Panama") is True
    assert check_palindrome(" ") is True
