def calc_max_size_distinct_letters_substr(s: str) -> int:
    """
    Let's keep track indexes of elements that we've already seen. We'll move pointer and check if we've already seen
    current element. If so, update position.
    In this approach we don't have to update dictionary.


    index_    0    1    2    3   4   5   6   7
    string    a    c    b    d   b   a   c   d
              ^                  ^
              |                  |
            left               right
            seen = {a : 0, c : 1, b : 2, d: 3}
            # case 1: seen[b] = 2, current window  is s[0:4] ,
            #        b is inside current window, seen[b] = 2 > left = 0. Move left pointer to seen[b] + 1 = 3
            seen = {a : 0, c : 1, b : 4, d: 3}
    index_    0    1    2    3   4   5   6   7
    string    a    c    b    d   b   a   c   d
                             ^   ^
                             |   |
                          left  right
    index_    0    1    2    3   4   5   6   7
    string    a    c    b    d   b   a   c   d
                             ^       ^
                             |       |
                           left    right
            # case 2: seen[a] = 0, which means <a> is not in current window s[3:5] , since seen[a] = 0 < left = 3
            # we can keep moving right pointer.


    Time complexity: O(n)
    Space complexity: O(n)
    """
    seen = {}
    left = max_size = 0
    for right in range(len(s)):
        if s[right] not in seen:
            max_size = max(max_size, right - left + 1)
        else:
            if left <= seen[s[right]]:
                left = seen[s[right]] + 1
            else:
                max_size = max(max_size, right - left + 1)

        seen[s[right]] = right  # add position of current letter
    return max_size


if __name__ == '__main__':
    assert calc_max_size_distinct_letters_substr("abcabcbb") == 3
    assert calc_max_size_distinct_letters_substr("bbbbb") == 1
    assert calc_max_size_distinct_letters_substr("pwwkew") == 3
    assert calc_max_size_distinct_letters_substr("") == 0
    assert calc_max_size_distinct_letters_substr("a") == 1
