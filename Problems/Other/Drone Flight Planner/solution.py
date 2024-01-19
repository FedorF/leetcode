from typing import List


def calc_min_energy(route: List[List[int]]) -> float:
    """
    Since drone doesn't spend energy on flat movement, we are only interested in z coordinate.

    Time complexity: O(n)
    Space complexity: O(1)
    """
    battery = energy_needed = 0
    for i in range(1, len(route)):
        high = route[i][2] - route[i - 1][2]  # calculate step i high
        if high <= 0:  # descending, so battery charging
            battery += -high
        else:  # ascending, so spending battery's energy
            battery -= high
            if battery < 0:
                energy_needed += -battery
                battery = 0
    return energy_needed


if __name__ == '__main__':
    route = [[0, 2, 10],
             [3, 5, 0],
             [9, 20, 6],
             [10, 12, 15],
             [10, 10, 8]]
    assert calc_min_energy(route) == 5
