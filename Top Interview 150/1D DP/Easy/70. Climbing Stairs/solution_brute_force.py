def count_routes(n: int) -> int:
    """
    Brute Force approach: depth-first-search.
    Start with 0 step. At each step check two routes: +1 step or +2 steps.

    Time complexity: O(2^n)
    Space complexity: O(1)

    !!!Raises "Time Limit Exceeded" on leetcode.
    """

    def dfs(cur_step: int = 0):
        nonlocal res  # use nonlocal in order to reach variable from enclosing (non-local) scope (outer function)

        if cur_step == n:
            res += 1
            return

        if cur_step > n:
            return

        dfs(cur_step + 1)
        dfs(cur_step + 2)

    res = 0
    dfs()
    return res


if __name__ == '__main__':
    assert count_routes(1) == 1
    assert count_routes(2) == 2
    assert count_routes(3) == 3
    assert count_routes(4) == 5
