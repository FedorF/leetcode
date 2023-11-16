from typing import List


def calc_min_candies(ratings: List[int]) -> int:
    """
    We should make two passes:
     1) During the first one, we walk forward defining list with candies and comparing current rating with
    left one. If current is greater, then current candies value would be 1 more greater.
     2) On the second pass we walk backward comparing current rating with the right one. If current rating is greater
     and current value of candies is less, then current candies value would be 1 more greater than the right one.


    Time complexity: O(N)
    Space complexity: O(N)
    """
    candies = [1]
    for i in range(1, len(ratings)):
        if ratings[i] > ratings[i - 1]:
            candies.append(candies[i - 1] + 1)
        else:
            candies.append(1)

    total = candies[-1]
    for i in range(len(ratings) - 2, -1, -1):
        if (ratings[i] > ratings[i + 1]) and (candies[i] <= candies[i + 1]):
            candies[i] = candies[i + 1] + 1
        total += candies[i]
    return total


if __name__ == '__main__':
    assert calc_min_candies([1, 0, 2]) == 5
    assert calc_min_candies([1, 2, 2]) == 4
    assert calc_min_candies([100]) == 1
    assert calc_min_candies([0]) == 1
    assert calc_min_candies([5, 3, 2, 1]) == 10
    assert calc_min_candies([1, 2, 3, 5]) == 10
    assert calc_min_candies([5, 5]) == 2
    assert calc_min_candies([1, 3, 2, 2, 1]) == 7
