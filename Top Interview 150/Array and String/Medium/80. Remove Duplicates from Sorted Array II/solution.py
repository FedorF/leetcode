from typing import List


def remove_duplicates(xs: List[int]) -> int:
    """
    We should update the vacant position pointer every step, except when current counter > 2
    Function should return number of element in list after transformation, not a number of unique elements!

    Time: O(n)
    Space: O(1)
    """

    cnt = 0
    vacant_pos = 0
    for i in range(vacant_pos, len(xs)):
        if i > 0 and xs[i] > xs[i - 1]:
            cnt = 1
        else:
            cnt += 1
        xs[vacant_pos] = xs[i]
        if cnt <= 2:
            vacant_pos += 1
    return vacant_pos


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = remove_duplicates(nums)
    assert k == 5 and nums[:5] == [1, 1, 2, 2, 3]

    nums = [1, 2, 2, 2, 2, 3, 4, 5, 5]
    k = remove_duplicates(nums)
    assert k == 7 and nums[:7] == [1, 2, 2, 3, 4, 5, 5]

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    k = remove_duplicates(nums)
    assert k == 7 and nums[:7] == [0, 0, 1, 1, 2, 3, 3]

    nums = [0]
    k = remove_duplicates(nums)
    assert k == 1 and nums[:1] == [0]

    nums = [0, 0]
    k = remove_duplicates(nums)
    assert k == 2 and nums[:2] == [0, 0]

    nums = [0, 1]
    k = remove_duplicates(nums)
    assert k == 2 and nums[:2] == [0, 1]

    nums = [0, 0, 0]
    k = remove_duplicates(nums)
    assert k == 2 and nums[:2] == [0, 0]

    nums = [0, 0, 1]
    k = remove_duplicates(nums)
    assert k == 3 and nums[:3] == [0, 0, 1]
