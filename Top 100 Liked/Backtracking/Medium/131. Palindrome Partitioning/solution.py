from typing import List


def partition_palindrome(s: str) -> List[List[str]]:
    """

    Time complexity: O(2^n)
    Space complexity: O(2^n)

    """

    def is_palindrome(line: str):
        left, right = 0, len(line) - 1
        while left < right:
            if line[left] != line[right]:
                return False
            left += 1
            right -= 1

        return True

    def backtrack(i: int = 0):
        if i >= len(s):
            xs = []
            for i in range(len(partitions)):
                if not is_palindrome(partitions[i]):  # check if partition is palindrome
                    return
                xs.append("".join(partitions[i]))  # convert to string

            res.append(xs)
            return

        # there are two options for current element:
        if len(partitions) > 0:  # add to current partition
            partitions[-1].append(s[i])
            backtrack(i + 1)
            partitions[-1].pop()

        partitions.append([s[i]])  # start new partition
        backtrack(i + 1)
        partitions.pop()
        return

    res, partitions = [], []
    backtrack()
    return res


if __name__ == '__main__':
    actual, expected = partition_palindrome("aab"), [["a", "a", "b"], ["aa", "b"]]
    assert sorted(actual) == sorted(expected), f"actual: {actual}, expected: {expected}"

    actual, expected = partition_palindrome("a"), [["a"]]
    assert actual == expected, f"actual: {actual}, expected: {expected}"
