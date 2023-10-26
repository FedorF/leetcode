def can_build(ransom_note: str, magazine: str) -> bool:
    """
    Let's define dictionary that maps letter from magazine to quantity.
    Time complexity: O(N) + O(M) = O(max(len(ransom_note), len(magazine)))
    """
    letters = {}
    for x in magazine:
        if x in letters:
            letters[x] += 1
        else:
            letters[x] = 1

    for x in ransom_note:
        if letters.get(x, 0) == 0:
            return False
        letters[x] -= 1

    return True


if __name__ == '__main__':
    assert can_build(ransom_note="a", magazine="b") is False
    assert can_build(ransom_note="aa", magazine="ab") is False
    assert can_build(ransom_note="aa", magazine="aab") is True
