import heapq
from typing import List, Tuple


def find_max_capital(k: int, w: int, profits: List[int], capital: List[int]) -> int:
    """
    Greedy approach.
    Define and fill max-heap using profit as a key. Then iteratively run projects.
    At each run we one-by-one pull the most profitable project from heap and check if we have enough balance to finish
    it. If not put this project to to-be-done heap, and process net project.
    After finishing cycle check if we have more projects to do, or we can't finish any of them because we don't have
    enough balance.


    Time complexity: O(n*log(n))
    Space complexity: O(N)


    """
    n = len(profits)

    projects = []
    heapq.heapify(projects)
    for i in range(n):
        heapq.heappush(projects, (-profits[i], (profits[i], capital[i])))

    def run_projects(cur_projects: List[Tuple], cur_k: int, balance: int):
        tbd = []
        heapq.heapify(tbd)
        while cur_projects and cur_k > 0:
            _, (profit, cost) = heapq.heappop(cur_projects)
            if balance >= cost:
                balance += profit
                cur_k -= 1
            else:
                heapq.heappush(tbd, (-profit, (profit, cost)))
        return tbd, cur_k, balance

    prev_k = k
    while True:
        projects, k, w = run_projects(projects, k, w)
        if k == prev_k or len(projects) == 0:
            break
        prev_k = k

    return w


if __name__ == '__main__':
    assert find_max_capital(k=2, w=0, profits=[1, 2, 3], capital=[0, 1, 1]) == 4
    assert find_max_capital(k=3, w=0, profits=[1, 2, 3], capital=[0, 1, 2]) == 6
    assert find_max_capital(k=1, w=2, profits=[1, 2, 3], capital=[1, 1, 2]) == 5
