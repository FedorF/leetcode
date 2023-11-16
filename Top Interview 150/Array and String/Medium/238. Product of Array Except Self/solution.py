from typing import List


def calc_excluded_product(nums: List[int]) -> List[int]:
    """
    Let's walk through the list and calculate total product. Then, make second pass and divide total product by current
    element and save the result in current index.

    We should use additional logic for the case, when there is one or more zeros in the list.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    product = 1
    zero_cnt = 0
    zero_ind = 0
    for i, x in enumerate(nums):
        if x != 0:
            product *= x
        else:
            zero_cnt += 1
            if zero_cnt > 1:
                return len(nums)*[0]
            zero_ind = i

    if zero_cnt == 1:
        output = len(nums)*[0]
        output[zero_ind] = product
        return output

    for i in range(len(nums)):
        nums[i] = int(product / nums[i])

    return nums


if __name__ == '__main__':
    assert calc_excluded_product([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert calc_excluded_product([0, 0, -1, -100]) == [0, 0, 0, 0]
    assert calc_excluded_product([1, -1, 0, 10]) == [0, 0, -10, 0]
