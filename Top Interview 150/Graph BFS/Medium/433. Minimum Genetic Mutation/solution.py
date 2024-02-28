from collections import deque
from typing import List


def calc_min_mutation(start_gene: str, end_gene: str, bank: List[str]) -> int:
    """
    BFS approach.


    Time complexity: O()
    Space complexity: O()

    """


if __name__ == '__main__':
    actual, expected = calc_min_mutation(
        "AACCGGTT",
        "AACCGGTA",
        ["AACCGGTA"]
    ), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_min_mutation(
        "AACCGGTT",
        "AAACGGTA",
        ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    ), 2
    assert actual == expected, f"expected: {expected}, actual: {actual}"
