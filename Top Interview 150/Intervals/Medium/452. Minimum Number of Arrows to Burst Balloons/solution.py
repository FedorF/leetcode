from typing import List


def calc_min_shots(balloons: List[List[int]]) -> int:
    """
    See Readme.md

    Time complexity: O(n*log(n)) due to sorting
    Space complexity: O(1)
    """
    balloons = sorted(balloons, key=lambda x: x[0])
    shooting_area_st, shooting_area_end = balloons[0]
    arrows_cnt = 0
    for i in range(1, len(balloons)):
        balloon_st, balloon_end = balloons[i]
        if max(shooting_area_st, balloon_st) <= min(shooting_area_end, balloon_end):  # if overlap
            shooting_area_st = max(shooting_area_st, balloon_st)  # update shooting area
            shooting_area_end = min(shooting_area_end, balloon_end)
        else:
            arrows_cnt += 1
            shooting_area_st, shooting_area_end = balloons[i]
    arrows_cnt += 1  # to shoot last one (balloon/shooting area)
    return arrows_cnt


if __name__ == '__main__':
    assert calc_min_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert calc_min_shots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert calc_min_shots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert calc_min_shots([[1, 2]]) == 1
