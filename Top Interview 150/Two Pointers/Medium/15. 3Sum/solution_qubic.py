from typing import List


def find_triplets(nums: List[int]) -> List[List[int]]:
    """
    Brute Force solution. Check every possible triplets. Define "seen" set to check if current triplet is already seen.
    Raises "Time Limit Exceeded" error on leetcode test cases.

    Time complexity: O(n^3)
    Space complexity: O(n)
    """
    seen = set()
    output = []
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    if (nums[i], nums[j]) in seen or (nums[j], nums[i]) in seen:
                        continue
                    elif (nums[i], nums[k]) in seen or (nums[k], nums[i]) in seen:
                        continue
                    elif (nums[k], nums[j]) in seen or (nums[j], nums[k]) in seen:
                        continue
                    else:
                        output.append([nums[i], nums[j], nums[k]])
                        seen.add((nums[i], nums[j]))
                        seen.add((nums[j], nums[i]))
                        seen.add((nums[i], nums[k]))
                        seen.add((nums[k], nums[i]))
                        seen.add((nums[k], nums[j]))
                        seen.add((nums[j], nums[k]))
    return output


if __name__ == '__main__':
    assert find_triplets([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, 2, -1]]
    assert find_triplets([0, 1, 1]) == []
    assert find_triplets([0, 0, 0]) == [[0, 0, 0]]
