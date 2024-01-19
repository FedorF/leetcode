from typing import List


def contains_duplicates_nearby(nums: List[int], dist: int) -> bool:
    """
    Define dictionary with already seen numbers

    Time complexity: O(N)
    Space complexity: O(N)

    """
    if len(nums) <= 1:
        return False

    seen = {}
    for i, x in enumerate(nums):
        duplicate_ind = seen.get(x, -1)
        if duplicate_ind >= 0 and abs(duplicate_ind - i) <= dist:
            return True
        else:
            seen[x] = i

    return False


if __name__ == '__main__':
    assert contains_duplicates_nearby([1, 2, 3, 1], 3) is True
    assert contains_duplicates_nearby([1, 0, 1, 1], 1) is True
    assert contains_duplicates_nearby([1, 2, 3, 1, 2, 3], 2) is False
    assert contains_duplicates_nearby([1], 0) is False
    assert contains_duplicates_nearby([1, 2, 3, 4, 5, 1], 4) is False
    assert contains_duplicates_nearby([1, 2, 3, 4, 5, 1], 6) is True
    assert contains_duplicates_nearby([99, 99], 2) is True
