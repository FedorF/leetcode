from collections import defaultdict
from typing import List


def can_finish_courses(n: int, prerequisites: List[List[int]]) -> bool:
    """

    Time complexity: O(n*E)
    Space complexity: O(n)

    """
    pre2crs = defaultdict(list)  # prerequisite to course mapping
    crs2pre = defaultdict(set)  # course to prerequisite mapping
    finished = set(range(n))  # finished courses
    # fill maps
    for course, pre in prerequisites:
        pre2crs[pre].append(course)
        crs2pre[course].add(pre)
        if course in finished:
            finished.remove(course)

    while finished:
        pre = finished.pop()  # consider finished prerequisite
        if pre in pre2crs:
            for course in pre2crs.pop(pre):  # consider all courses that require current prerequisite
                if course in crs2pre:
                    crs2pre[course].remove(pre)  # remove current prerequisite from course's prerequisites
                    if len(crs2pre[course]) == 0:  # no prerequisite left
                        finished.add(course)  # so add course to finished
                        crs2pre.pop(course)

    return len(crs2pre) == 0


if __name__ == '__main__':
    actual, expected = can_finish_courses(2, [[1, 0]]), True
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_finish_courses(2, [[1, 0], [0, 1]]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = can_finish_courses(3, [[1, 0], [1, 2], [0, 1]]), False
    assert actual == expected, f"expected: {expected}, actual: {actual}"
