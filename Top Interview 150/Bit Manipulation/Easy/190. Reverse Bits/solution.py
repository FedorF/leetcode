def reverse_bit(s: str) -> int:
    out = 0
    power = 0
    for x in s:
        out += int(x) * 2**power
        power += 1
    return out


if __name__ == '__main__':
    assert reverse_bit("00000010100101000001111010011100") == 964176192
    assert reverse_bit("11111111111111111111111111111101") == 3221225471
