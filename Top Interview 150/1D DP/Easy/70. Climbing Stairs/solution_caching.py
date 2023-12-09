def count_routes(n: int) -> int:
    """
    Memoization (caching) approach.
    Start with 0 step. At each step check two routes: with 1 step and 2 steps and cache result of computation to reuse
    it later during next steps.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    cache = {}

    def backtrack(cur_step: int = 0, routes: int = 0) -> int:
        if cur_step in cache:
            return routes + cache[cur_step]

        if cur_step == n:
            return routes + 1

        if cur_step > n:
            return routes

        cache[cur_step] = routes + backtrack(cur_step + 1, routes) + backtrack(cur_step + 2, routes)
        return cache[cur_step]

    return backtrack()


if __name__ == '__main__':
    assert count_routes(1) == 1
    assert count_routes(2) == 2
    assert count_routes(3) == 3
    assert count_routes(4) == 5
