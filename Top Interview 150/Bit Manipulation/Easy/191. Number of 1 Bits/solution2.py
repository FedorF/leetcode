def calc_hamming_weight(n: int) -> int:
    """

    Time complexity: O(1)
    Space complexity: O(1)

    """
    cnt = 0
    while n:
        if n & 1:
            cnt += 1
        n = n >> 1

    return cnt
