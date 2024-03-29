def reverse_bit(n: int) -> int:
    """

    Time complexity: O(1)
    Space complexity: O(1)

    """
    n = format(n, "032b")
    out = 0
    power = 0
    for x in n:  # traverse through 32 bits
        out += int(x) * (2 ** power)
        power += 1

    return out
