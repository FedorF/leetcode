from typing import List


def calc_min_speed(piles: List[int], h: int) -> int:
    """
    Brute force solution.

    The monkey can only process one pile per hour, so:
        1) if h < len(piles), it can't process all the piles
        2) if h == len(piles), speed must be equal to max(piles), in order to be able to process all piles
        3) In order to reduce time complexity of this step, we can apply binary search here, instead of iterating
        through all possible values of speed.
        The minimum speed we should check is 1 and the maximum is max(piles).


    Time complexity: O(log(max(piles)) * len(piles))
    Space complexity: O(1)

    """
    if h < len(piles):
        return -1

    if h == len(piles):
        return max(piles)

    # apply binary search to reduce the complexity
    left, right = 1, max(piles)
    while left <= right:
        speed = left + (right - left) // 2
        total_hours = 0
        for pile in piles:
            cur_hours = pile // speed
            if pile % speed > 0:
                cur_hours += 1

            total_hours += cur_hours
            if total_hours > h:
                break

        if total_hours > h:  # increase the speed
            left = speed + 1
        else:  # reduce the speed
            right = speed - 1

    return left


if __name__ == '__main__':
    actual, expected = calc_min_speed(piles=[3, 6, 7, 11], h=8), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_speed(piles=[30, 11, 23, 4, 20], h=6), 23
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_speed(piles=[30, 11, 23, 4, 20], h=5), 30
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_speed(piles=[30, 11, 23, 4, 20], h=6), 23
    assert actual == expected, f"expected: {expected}, actual: {actual}"
