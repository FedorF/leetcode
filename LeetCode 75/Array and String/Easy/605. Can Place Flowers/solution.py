from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    """
    Iterate through elements and check neighboring places, if there is no neighbors place flower and continue.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    if n == 0:
        return True

    if len(flowerbed) == 1:
        if (flowerbed[0] == 0) and (n == 1):
            return True
        return False

    for i in range(len(flowerbed)):
        if n <= 0:
            return True

        if flowerbed[i] == 1:
            continue

        if i == 0:  # first element
            if flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue

        if i == len(flowerbed) - 1:  # last element
            if flowerbed[i - 1] == 0:
                flowerbed[i] = 1
                n -= 1
                continue

        if (flowerbed[i - 1] == 0) and (flowerbed[i + 1] == 0):  # middle element
            flowerbed[i] = 1
            n -= 1

    return n <= 0


if __name__ == '__main__':
    actual, expected = can_place_flowers(flowerbed=[1, 0, 0, 0, 1], n=1), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[1, 0, 0, 0, 1], n=2), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[1, 0, 0, 0, 0, 1], n=2), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[1, 0, 0, 0, 0, 0, 1], n=2), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[0], n=1), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[0], n=0), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[0], n=2), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[1], n=0), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[1], n=1), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[0, 0], n=2), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[0, 0], n=1), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_place_flowers(flowerbed=[1, 1], n=1), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
