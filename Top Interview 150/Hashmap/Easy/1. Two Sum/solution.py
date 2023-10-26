from typing import List


def find_terms(nums: List[int], target: int) -> List[int]:
    """
    Define dictionary with already differences between target and already seen element.
    Check if current element in cache.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    cache = {}
    for i, x in enumerate(nums):
        if x in cache:
            return [cache[x], i]
        else:
            cache[target-x] = i
    return [-1]


if __name__ == '__main__':
    assert find_terms([1], 100) == [-1]
    assert find_terms([2,7,11,15], 9) == [0,1]
    assert find_terms([3,2,4], 6) == [1,2]
    assert find_terms([3,3,3],6) == [0,1]
