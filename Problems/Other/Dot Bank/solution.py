def convert_n(x: int):
    """
    Преобразовать входное число в запись, где разряды тысячи выделены запятыми

    """
    x = str(x)
    if len(x) <= 3:
        return x

    res = []
    window = 0
    i = len(x) - 1
    while i >= 0:
        if window == 3:
            res.append(",")
            window = 0
        else:
            res.append(x[i])
            window += 1
            i -= 1

    return "".join(reversed(res))


if __name__ == '__main__':
    actual = convert_n(123445567)
    expected = "123,445,567"
    assert actual == expected, f"actual: {actual}, expected:{expected}"

    actual = convert_n(12)
    expected = "12"
    assert actual == expected, f"actual: {actual}, expected:{expected}"

    actual = convert_n(3000)
    expected = "3,000"
    assert actual == expected, f"actual: {actual}, expected:{expected}"

    actual = convert_n(30000)
    expected = "30,000"
    assert actual == expected, f"actual: {actual}, expected:{expected}"
