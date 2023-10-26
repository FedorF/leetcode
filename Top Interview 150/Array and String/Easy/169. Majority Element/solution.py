from typing import List


def find_major_element(xs: List[int]) -> int:
    major = xs[0]
    cnt = {}
    for x in xs:
        if x not in cnt:
            cnt[x] = 1
        else:
            cnt[x] += 1
            if cnt[x] > len(xs) / 2:
                major = x
    return major


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    assert find_major_element(nums) == 2

    nums = [1, 2, 2]
    assert find_major_element(nums) == 2
