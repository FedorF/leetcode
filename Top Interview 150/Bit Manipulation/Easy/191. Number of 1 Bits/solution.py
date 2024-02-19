def calc_hamming_weight(n: int) -> int:
    """

    Time complexity: O(1)
    Space complexity: O(1)

    """
    n = format(n, "032b")
    cnt = 0
    for x in n:  # traverse through 32 bits
        if x == "1":
            cnt += 1

    return cnt
