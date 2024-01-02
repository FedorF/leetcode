from typing import List


def collide_asteroids(asteroids: List[int]) -> List[int]:
    """
    Stack approach.

    Time complexity: O(n)
    Space complexity: O(n)

    """
    stack = []
    i = 0
    while i < len(asteroids):  # run through all elements
        if len(stack) == 0:
            stack.append(asteroids[i])
            i += 1

        elif (stack[-1] * asteroids[i] > 0) or (stack[-1] < 0 < asteroids[i]):  # asteroids will never collides:
            stack.append(asteroids[i])  # either both go in the same direction,
            i += 1  # or left goes to the left and right goes opposite

        elif stack[-1] + asteroids[i] == 0:  # both explodes, due to the equal sizes
            stack.pop()
            i += 1

        elif abs(stack[-1]) > abs(asteroids[i]):  # asteroid in the stack is bigger, so the new one explodes
            i += 1

        else:  # new asteroid is bigger, so the one in stack explodes
            stack.pop()

    return stack


if __name__ == '__main__':
    actual, expected = collide_asteroids([-10, 10]), [-10, 10]  # left one goes to the left, and right goes opposite
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = collide_asteroids([-2, -1, 1, 2]), [-2, -1, 1, 2]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = collide_asteroids([5, 10, -5]), [5, 10]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = collide_asteroids([8, -8]), []
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = collide_asteroids([10, 2, -5]), [10]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = collide_asteroids([10, 10]), [10, 10]  # both go in the same direction
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = collide_asteroids([10, -5]), [10]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = collide_asteroids([10, -10]), []
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = collide_asteroids([10, -100]), [-100]
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = collide_asteroids([10, -10, 10, -10]), []
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = collide_asteroids([10, 20, -100]), [-100]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
