from typing import List


def can_complete_circle(gas: List[int], cost: List[int]) -> int:
    """
    In order to determine if it's possible to make a full circle, we should walk through all the stations and calculate
    total volume of gas. If it's not negative, so we're good.
    In order to find starting gas station, we should find an index, where there is the smallest amount of gasoline.

    Time complexity: O(N)
    Space complexity: O(1)
    """

    gas_volume = 0
    min_gas_volume = 0
    ind = 0
    for i in range(len(gas)):
        if gas_volume <= min_gas_volume:
            ind = i
            min_gas_volume = gas_volume
        gas_volume += gas[i] - cost[i]
    if gas_volume >= 0:
        return ind
    return -1


if __name__ == '__main__':
    assert can_complete_circle(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]) == 3
    assert can_complete_circle(gas=[2, 3, 4], cost=[3, 4, 3]) == -1
    assert can_complete_circle(gas=[0], cost=[100]) == -1
    assert can_complete_circle(gas=[100], cost=[50]) == 0
    assert can_complete_circle(gas=[5, 1, 2, 3, 4], cost=[4, 4, 1, 5, 1]) == 4
    assert can_complete_circle(gas=[0, 100], cost=[50, 50]) == 1
