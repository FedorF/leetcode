def is_isomorphic(first: str, second: str) -> bool:
    """
    Let's define 2 dictionaries. One would map characters from s to t. And the second one: from t to s.

    Time complexity: O(N)
    Space complexity: O(N)
    """
    if len(first) != len(second):
        return False

    straight = {}
    inverse = {}
    for i in range(len(first)):
        second_map = straight.get(first[i])
        first_map = inverse.get(second[i])
        if not second_map and not first_map:
            straight[first[i]] = second[i]
            inverse[second[i]] = first[i]
        elif second_map and first_map:
            if second_map != second[i] or first_map != first[i]:
                return False
        else:
            return False

    return True


if __name__ == '__main__':
    assert is_isomorphic("egg", "add") is True
    assert is_isomorphic("foo", "bar") is False
    assert is_isomorphic("paper", "title") is True
    assert is_isomorphic(" ", ".") is True
    assert is_isomorphic("AAA", "   ") is True
