def roman_to_int(s: str) -> int:
    dict_single = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    dict_pair = {
        ('I', 'V'): 4,
        ('I', 'X'): 9,
        ('X', 'L'): 40,
        ('X', 'C'): 90,
        ('C', 'D'): 400,
        ('C', 'M'): 900,
    }
    len_s = len(s)
    if len_s == 1:
        return dict_single[s]

    out = i = 0
    while i < len_s:
        pair = (s[i], s[i + 1])
        if (i < len_s-1) and (pair in dict_pair):
            out += dict_pair[pair]
            i += 2
        else:
            out += dict_single[s[i]]
            i += 1

    return out


if __name__ == '__main__':
    assert roman_to_int("III") == 3
    assert roman_to_int("LVIII") == 58
    assert roman_to_int("MCMXCIV") == 1994
