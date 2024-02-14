from typing import List


def can_visit_all_rooms(rooms: List[List[int]]) -> bool:
    """
    DFS Graph approach. Store already visited rooms and opened (for exploration) rooms.
    Traverse through opened rooms and save obtained keys.


    Time complexity: O(rooms^2)
    Space complexity: O(rooms)

    """
    opened = [0]
    visited = set()

    while opened:
        room_ind = opened.pop()
        visited.add(room_ind)
        for key in rooms[room_ind]:
            if key not in visited:
                opened.append(key)

    return len(visited) == len(rooms)


if __name__ == '__main__':
    xs = [[6, 7, 8], [5, 4, 9], [], [8], [4], [], [1, 9, 2, 3], [7], [6, 5], [2, 3, 1]]
    actual, expected = can_visit_all_rooms(rooms=xs), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_visit_all_rooms(rooms=[[1], [2], [3], []]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_visit_all_rooms(rooms=[[1, 3], [3, 0, 1], [2], [0]]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
