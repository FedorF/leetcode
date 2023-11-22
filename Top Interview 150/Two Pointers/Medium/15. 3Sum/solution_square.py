from typing import List


def find_triplets(nums: List[int]) -> List[List[int]]:
    """

    Time complexity: O(n^2)
    Space complexity: O(n)
    """
    triplets = []
    seen_numbers = set()
    seen_combinations = set()
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if -nums[i] - nums[j] in seen_numbers:
                if ((nums[i], nums[j]) not in seen_combinations) and ((nums[j], nums[i]) not in seen_combinations):
                    triplets.append([-nums[i] - nums[j], nums[i], nums[j]])
                    seen_combinations.add((nums[i], nums[j]))
                    seen_combinations.add((nums[j], nums[i]))
                    seen_combinations.add((nums[i], -nums[i] - nums[j]))
                    seen_combinations.add((-nums[i] - nums[j], nums[i]))
                    seen_combinations.add((-nums[i] - nums[j], nums[j]))
                    seen_combinations.add((nums[j], -nums[i] - nums[j]))
        seen_numbers.add(nums[i])
    return triplets


if __name__ == '__main__':
    assert find_triplets([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, 2, -1]]
    assert find_triplets([0, 1, 1]) == []
    assert find_triplets([0, 0, 0]) == [[0, 0, 0]]
