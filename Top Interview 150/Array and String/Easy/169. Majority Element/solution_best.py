from typing import List


def find_major_element(xs: List[int]) -> int:
    """
    Moore Voting Algorithm
    Constant space and Linear time
    The intuition behind the Moore's Voting Algorithm is based on the fact that if there is a majority element in an
    the array, it will always remain in the lead, even after encountering other elements.
    """
    cnt = major = 0
    for x in xs:
        if cnt == 0:
            major = x
        if x == major:
            cnt += 1
        else:
            cnt -= 1
    return major


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    assert find_major_element(nums) == 2

    nums = [1, 2, 2]
    assert find_major_element(nums) == 2
