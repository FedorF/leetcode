def convert_to_zigzag(s: str, n_rows: int) -> str:
    """
    Let's define dictionary that maps row_index to its letters. Then we should walk through input string and

    """
    if n_rows == 1:
        return s
    n_rows = min(n_rows, len(s))
    rows = {}
    i = 0
    going_up = False
    for letter in s:
        if i in rows:
            rows[i] += letter
        else:
            rows[i] = letter

        if going_up:
            if i == 0:
                going_up = False
                i += 1
            else:
                i -= 1
        else:
            if i == n_rows - 1:
                going_up = True
                i -= 1
            else:
                i += 1

    return "".join([rows[i] for i in range(n_rows)])


if __name__ == '__main__':
    assert convert_to_zigzag("PAYPALISHIRING", 1) == "PAYPALISHIRING"
    assert convert_to_zigzag("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG"
    assert convert_to_zigzag("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert_to_zigzag("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert_to_zigzag("A", 1) == "A"
    assert convert_to_zigzag("A", 2) == "A"
