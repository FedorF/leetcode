from typing import List


def find_single_number(nums: List[int]) -> int:
    """
    Bit manipulation approach.

    XOR of any two num gives the difference of bit as 1 and same bit as 0.
    Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
    So, we will always get the single element because all the same ones will evaluate to 0
    and 0 ^ single_number = single_number.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    xor = 0
    for x in nums:
        xor ^= x

    return xor


if __name__ == '__main__':
    assert find_single_number([2, 2, 1]) == 1
    assert find_single_number([2, 2, 1, 5, 3, 1, 3]) == 5
