from typing import List


def find_longest_common_prefix(xs: List[str]) -> str:
    """
    Time complexity: O(len(xs) * min(len(xs_i)))

    """
    if len(xs) == 1:
        return xs[0]

    prefix = ""
    for letters in zip(*xs):
        if len(set(letters)) == 1:
            prefix += letters[0]
        else:
            break

    return prefix


if __name__ == '__main__':
    xs = ["flower", "flow", "flight"]
    assert find_longest_common_prefix(xs) == 'fl'

    xs = ["dog", "racecar", "car"]
    assert find_longest_common_prefix(xs) == ''

    xs = ["dog"]
    assert find_longest_common_prefix(xs) == 'dog'

    xs = [""]
    assert find_longest_common_prefix(xs) == ''

    xs = ["", ""]
    assert find_longest_common_prefix(xs) == ''

    xs = ['plow', 'flower', 'flight']
    assert find_longest_common_prefix(xs) == ''
