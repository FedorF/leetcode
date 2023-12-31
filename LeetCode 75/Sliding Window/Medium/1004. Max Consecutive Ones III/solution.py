from typing import List


def max_consecutive_ones(xs: List[int], k_flips: int) -> int:
    """
    Sliding window approach. Move right bound until we spend all flips. Then start moving left bound until we get new
    flip. Keep track on current length.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    max_len = cur_len = 0
    if k_flips == 0:  # edge case, when we don't have any flips, just iterate through elements and find max len.
        for i in range(len(xs)):
            if xs[i] == 0:
                max_len = max(max_len, cur_len)
                cur_len = 0
            else:
                cur_len += 1

        return max(max_len, cur_len)

    cur_flips = k_flips
    left = right = 0
    while right < len(xs):
        if xs[right] == 1:  # keep moving right bound
            cur_len += 1
            right += 1

        elif cur_flips > 0:  # keep moving right bound
            cur_flips -= 1
            cur_len += 1
            right += 1

        elif xs[left] == 0:  # move left bound
            cur_flips += 1
            cur_len -= 1
            left += 1

        else:  # keep moving left bound
            cur_len -= 1
            left += 1

        max_len = max(max_len, cur_len)

    return max_len


if __name__ == '__main__':
    actual, expected = max_consecutive_ones([0, 0, 0, 0, 0, 0], 6), 6
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_consecutive_ones([0, 0, 0, 0, 0, 0], 1), 1
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_consecutive_ones([0, 0, 0, 0, 0, 0], 0), 0
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_consecutive_ones([1, 1, 1, 1, 1, 1], 2), 6
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_consecutive_ones([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2), 6
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_consecutive_ones([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3), 10
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_consecutive_ones([0], 1), 1
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_consecutive_ones([1], 1), 1
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_consecutive_ones([1], 0), 1
    assert actual == expected, f"actual: {actual}, expected: {expected}"

    actual, expected = max_consecutive_ones([0], 0), 0
    assert actual == expected, f"actual: {actual}, expected: {expected}"
