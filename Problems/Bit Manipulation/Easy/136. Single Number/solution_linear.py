from typing import List


def find_single_number(nums: List[int]) -> int:
    """
    Hash-map approach.

    Time complexity: O(n)
    Space complexity: O(n)

    """
    candidates = set()
    for x in nums:
        if x in candidates:
            candidates.remove(x)
        else:
            candidates.add(x)

    return candidates.pop()


if __name__ == '__main__':
    assert find_single_number([2, 2, 1]) == 1
    assert find_single_number([2, 2, 1, 5, 3, 1, 3]) == 5
