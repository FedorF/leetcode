from typing import List


def compress(xs: List[str]) -> int:
    """
    Compress in-place and return len of resulted string.


    Time complexity: O(n)
    Space complexity: O(1)

    """
    if len(xs) == 1:
        return 1

    res = vacant_ind = 0
    cnt = 1
    for i in range(1, len(xs)):
        if xs[i] == xs[i - 1]:
            cnt += 1
        else:  # found another letter
            xs[vacant_ind] = xs[i - 1]  # insert prev letter to compressed string
            vacant_ind += 1
            if cnt > 1:  # insert letter's counter
                for j, digit in enumerate(str(cnt)):
                    xs[vacant_ind + j] = digit
                res += 1 + len(str(cnt))  # update length variable
                vacant_ind += len(str(cnt))  # update vacant position variable
            else:  # we have only one letter, so no need to insert counter
                res += 1
            cnt = 1  # update counter

        if i == len(xs) - 1:  # edge case, when it's last element
            xs[vacant_ind] = xs[i]
            vacant_ind += 1

            if cnt > 1:
                for j, digit in enumerate(str(cnt)):
                    xs[vacant_ind + j] = digit
                res += 1 + len(str(cnt))
            else:
                res += 1
    return res


if __name__ == '__main__':
    nums, compressed = ["a", "a", "b", "b", "c", "c", "c"], ["a", "2", "b", "2", "c", "3"]
    actual, expected = compress(nums), 6
    assert actual == expected and nums[:expected] == compressed, f"expected: {compressed}, actual: {nums[:expected]}"

    nums = ["a"]
    actual, expected = compress(nums), 1
    assert actual == expected and nums == ["a"], f"expected: {expected}, actual: {actual}"

    nums = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    compressed = ["a", "b", "1", "2"]
    actual, expected = compress(nums), 4
    assert actual == expected and nums[:expected] == compressed, f"expected: {compressed}, actual: {nums[:expected]}"
