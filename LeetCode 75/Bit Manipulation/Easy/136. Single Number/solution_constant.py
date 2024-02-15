from typing import List


def find_single_number(nums: List[int]) -> int:
    """
    Bit manipulation approach.

    The idea is to apply XOR bitwise operation.
    XOR has properties:
    1) a XOR a = 0
    2) a XOR 0 = a
    3) A^A^B = B^A^A = A^B^A = B  (position doesn't matter)

    Therefore, a^a^a......... (even times) = 0 and a^a^a........(odd times) = a


    For example,

    decimal = 21  =>  binary = 10101
    21 XOR 21   =>  10101
                    10101
                    -----
                    00000   =>  equal to 0

    21 XOR 0   =>  10101
                   00000
                   -----
                   10101   => equals to 21

    So, applying XOR operation to all values in nums, we'll always get single number in the end.


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
