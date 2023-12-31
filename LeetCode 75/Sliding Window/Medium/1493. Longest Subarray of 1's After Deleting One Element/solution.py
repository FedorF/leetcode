from typing import List


def max_len_sublist_after_del_one_el(xs: List[int]) -> int:
    """
    Sliding window approach.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    max_len = cur_len = zero_cnt = left = right = 0
    can_delete = True
    while right < len(xs):
        if xs[right] == 1:  # move right bound
            cur_len += 1
            right += 1

        elif can_delete:  # delete current zero element and keep moving right bound
            can_delete = False
            zero_cnt += 1
            right += 1

        elif xs[left] == 1:  # move left bound
            cur_len -= 1
            left += 1

        else:  # move left bound. Now we can delete new element due to left one was zero
            can_delete = True
            left += 1

        max_len = max(max_len, cur_len)

    if zero_cnt == 0:
        return len(xs) - 1

    return max_len


if __name__ == '__main__':
    actual, expected = max_len_sublist_after_del_one_el([1, 1, 0, 1]), 3
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_len_sublist_after_del_one_el([0, 1, 1, 1, 0, 1, 1, 0, 1]), 5
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_len_sublist_after_del_one_el([1, 1, 1]), 2
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_len_sublist_after_del_one_el([1]), 0
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_len_sublist_after_del_one_el([0]), 0
    assert actual == expected, f"actual: {actual}, expected: {expected}"
