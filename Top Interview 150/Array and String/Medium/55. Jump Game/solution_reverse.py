from typing import List


def can_jump_to_end(nums: List[int]) -> bool:
    """
    Let's start at the end of nums. Define the "steps" variable saying how many steps you need to get to the current
    "summit". Iterate within elements and find lower "summit" from which we could reach current one.
    Reset "steps" variable, so it's connected to the new "summit".

    Time complexity: O(N)
    Space complexity: O(1)
    """
    if len(nums) == 1:
        return True

    i = len(nums)-1
    steps = 0
    while i >= 0:
        if nums[i] < steps:
            steps += 1
        else:
            steps = 1
        i -= 1
    return steps == 1


if __name__ == '__main__':
    assert can_jump_to_end([2, 3, 1, 1, 4]) is True
    assert can_jump_to_end([3, 2, 1, 0, 4]) is False
    assert can_jump_to_end([0]) is True
    assert can_jump_to_end([0, 0]) is False
    assert can_jump_to_end([2, 5, 0, 0]) is True
    assert can_jump_to_end([2, 0, 0]) is True
