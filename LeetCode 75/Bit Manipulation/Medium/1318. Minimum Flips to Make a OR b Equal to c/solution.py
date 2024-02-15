def calc_min_flips(a: int, b: int, c: int) -> int:
    """

    Step 1:
      a | b is what we have while c is what we want.
      An XOR operation finds all different bits, i.e. (a | b) ^ c sets the bits where flip(s) is needed.
      Then we count the set bits.

    Step 2:
      There is only one case when two flips are needed: a bit is 0 in c but is 1 in both a and b.
      An AND operation finds all common 1 bits, i.e. a & b & ((a | b) ^ c) sets the common "1" bits in a, b
      and the must-flip bits found in Step 1.


    Time complexity: O(n_bits) = O(log(max(a, b, c)))
    Space complexity: O(1)

    """
    equation = (a | b) ^ c
    cnt = 0
    for x in format(equation, "b"):
        if x == "1":
            cnt += 1

    equation &= a & b
    for x in format(equation, "b"):
        if x == "1":
            cnt += 1

    return cnt


if __name__ == '__main__':
    actual, expected = calc_min_flips(a=2, b=6, c=5), 3
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_flips(a=1, b=2, c=3), 0
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_flips(a=4, b=2, c=7), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"
