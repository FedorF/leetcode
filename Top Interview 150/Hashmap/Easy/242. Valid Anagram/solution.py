def is_anagram(s: str, t: str) -> bool:
    """
    O(max(N, M))
    """
    if len(s) != len(t):
        return False

    letters = {}
    for x in s:
        if x in letters:
            letters[x] += 1
        else:
            letters[x] = 1

    for x in t:
        cnt = letters.get(x, 0)
        if cnt == 0:
            return False
        else:
            letters[x] -= 1

    return True


if __name__ == '__main__':
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram(" ", " ") is True
