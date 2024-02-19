def calc_binary_sum(a: str, b: str) -> str:
    """
    Define carry variable that store sum of digits and remainder from previous sum operation.


    Space Complexity: O(max(len(a), len(b)))
    Time Complexity: O(max(len(a), len(b)))

    """
    out = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1
    while i >= 0 or j >= 0 or carry > 0:
        if i >= 0:
            carry += int(a[i])
            i -= 1

        if j >= 0:
            carry += int(b[j])
            j -= 1

        out.append(f"{carry % 2}")
        carry //= 2

    return "".join(out[::-1])


if __name__ == '__main__':
    assert calc_binary_sum("11", "1") == "100"
    assert calc_binary_sum("1010", "1011") == "10101"
