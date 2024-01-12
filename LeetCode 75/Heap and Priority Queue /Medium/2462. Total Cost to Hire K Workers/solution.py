import heapq
from typing import List


def calc_hiring_cost(costs: List[int], workers_needed: List[int], candidates: int) -> int:
    """
    Min Heap approach.

    Time complexity: O(workers_needed * log(candidates))
    Space complexity: O(len(costs))

    """
    # define min heap for left candidates and right candidates
    # if there are fewer than "candidates" left for the right heap, fill it with the rest candidates
    left_candidates, right_candidates = costs[:candidates], costs[max(candidates, len(costs) - candidates):]
    heapq.heapify(left_candidates)
    heapq.heapify(right_candidates)

    l, r = candidates, len(costs) - candidates - 1  # keep track on current indexes for the left and right candidates
    total_cost = 0
    while (workers_needed > 0) and left_candidates and right_candidates:
        # compare candidates
        left = heapq.heappop(left_candidates)
        right = heapq.heappop(right_candidates)

        if left <= right:
            total_cost += left
            heapq.heappush(right_candidates, right)  # return right candidate back to his heap
            if l <= r:  # add new candidate to the left heap, if there left any
                heapq.heappush(left_candidates, costs[l])
                l += 1
        else:
            total_cost += right
            heapq.heappush(left_candidates, left)  # return left candidate back to his heap
            if r >= l:  # add new candidate to the right heap, if there left any
                heapq.heappush(right_candidates, costs[r])
                r -= 1

        workers_needed -= 1

    if workers_needed == 0:  # we're done
        return total_cost

    if left_candidates:  # no more candidates are in the right heap, so process the left heap only
        while workers_needed > 0:
            total_cost += heapq.heappop(left_candidates)
            workers_needed -= 1
        return total_cost

    while workers_needed > 0:  # no more candidates are in the left heap, so process the right heap only
        total_cost += heapq.heappop(right_candidates)
        workers_needed -= 1

    return total_cost


if __name__ == '__main__':
    actual, expected = calc_hiring_cost(costs=[1, 2, 4, 1], workers_needed=4, candidates=3), 8
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_hiring_cost(costs=[1, 2, 4, 1], workers_needed=4, candidates=1), 8
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_hiring_cost(costs=[1, 2, 4, 1], workers_needed=4, candidates=4), 8
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_hiring_cost(costs=[1, 2, 4, 1], workers_needed=1, candidates=4), 1
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_hiring_cost(costs=[17, 12, 10, 2, 7, 2, 11, 20, 8], workers_needed=3, candidates=4), 11
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual, expected = calc_hiring_cost(costs=[1, 2, 4, 1], workers_needed=3, candidates=3), 4
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    costs = [31, 25, 72, 79, 74, 65, 84, 91, 18, 59, 27, 9, 81, 33, 17, 58]
    actual, expected = calc_hiring_cost(costs, 11, 2), 423
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    costs = [28, 35, 21, 13, 21, 72, 35, 52, 74, 92, 25, 65, 77, 1, 73, 32, 43, 68, 8, 100, 84, 80, 14, 88, 42, 53, 98,
             69, 64, 40, 60, 23, 99, 83, 5, 21, 76, 34]
    actual, expected = calc_hiring_cost(costs, 32, 12), 1407
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    costs = [25, 65, 41, 31, 14, 20, 59, 42, 43, 57, 73, 45, 30, 77, 17, 38, 20, 11, 17, 65, 55, 85, 74, 32, 84]
    actual, expected = calc_hiring_cost(costs, 24, 8), 1035
    assert actual == expected, f"expected: {expected}, actual: {actual}"
