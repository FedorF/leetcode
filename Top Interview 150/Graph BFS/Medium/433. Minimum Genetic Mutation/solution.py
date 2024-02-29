from collections import deque
from typing import List


def calc_min_mutation(start_gene: str, end_gene: str, bank: List[str]) -> int:
    """
    BFS approach: for each position in start_gene check all possible mutations (4 letters).


    Time complexity: O(len(bank))
    Space complexity: O(len(bank))

    """
    bank = set(bank)
    queue = deque([(start_gene, 0)])
    seen = {start_gene}
    while queue:
        gene, n = queue.popleft()
        if gene == end_gene:
            return n

        for i in range(8):
            for c in ["A", "C", "G", "T"]:
                mutation = gene[:i] + c + gene[i + 1:]
                if (mutation in bank) and (mutation not in seen):
                    seen.add(mutation)
                    queue.append((mutation, n + 1))
    return -1


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
