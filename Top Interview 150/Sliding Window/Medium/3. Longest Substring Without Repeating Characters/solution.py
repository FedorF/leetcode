def calc_max_size_distinct_letters_substr(s: str) -> int:
    """
    Sliding window approach. We'll have two pointers: right and left. We'll move right pointer and check if new substr
    has distinct letters. If not, move left pointer until we get new distinct letters substr. Then continue loop.
    We'll use set to keep track on current substr, in order to O(1) look up if new letter is unique.
    It's a linear time approach, because both pointers and index <i> used for updating the dictionary linearly walk
    through elements.


    Time complexity: O(n)
    Space complexity: O(n)
    """
    cur_substr = {}
    left = max_size = 0
    for right in range(len(s)):
        if s[right] not in cur_substr:
            max_size = max(max_size, right - left + 1)
        else:  # move left pointer to the next position after doubled letter and update cur_substr
            left = cur_substr[s[right]] + 1
            cur_substr = {}
            for i in range(left, right):
                cur_substr[s[i]] = i

        cur_substr[s[right]] = right  # add position of current letter
    return max_size


if __name__ == '__main__':
    assert calc_max_size_distinct_letters_substr("abcabcbb") == 3
    assert calc_max_size_distinct_letters_substr("bbbbb") == 1
    assert calc_max_size_distinct_letters_substr("pwwkew") == 3
    assert calc_max_size_distinct_letters_substr("") == 0
    assert calc_max_size_distinct_letters_substr("a") == 1
