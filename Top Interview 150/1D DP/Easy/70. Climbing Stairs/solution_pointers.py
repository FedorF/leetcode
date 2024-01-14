def count_routes(n: int) -> int:
    """
    Dynamical Programming approach. See details in Readme.md. The main idea is that we have Fibonacci sequence

    Time complexity: O(n)
    Space complexity: O(1)
    """
    one, two = 1, 1
    for i in range(n - 1):
        one, two = one + two, one

    return one


if __name__ == '__main__':
    assert count_routes(1) == 1
    assert count_routes(2) == 2
    assert count_routes(3) == 3
    assert count_routes(4) == 5
