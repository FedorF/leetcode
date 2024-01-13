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

    # apply binary search to reduce time complexity
    left, right = 1, max(piles)
    speed_min = right
    while left <= right:
        speed = left + (right - left) // 2
        total_hours = 0
        for pile in piles:
            # calc time for processing current pile and add it to total time
            total_hours += pile // speed
            if pile % speed > 0:  # round up by 1 hour
                total_hours += 1

            if total_hours > h:
                break
        # increase speed
        if total_hours > h:
            left = speed + 1
        # reduce speed
        else:
            speed_min = speed  # save current speed as current minimal
            right = speed - 1

    return speed_min


if __name__ == '__main__':
    actual, expected = calc_min_speed(piles=[3, 6, 7, 11], h=8), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_speed(piles=[30, 11, 23, 4, 20], h=6), 23
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_speed(piles=[30, 11, 23, 4, 20], h=5), 30
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_speed(piles=[30, 11, 23, 4, 20], h=6), 23
    assert actual == expected, f"expected: {expected}, actual: {actual}"
