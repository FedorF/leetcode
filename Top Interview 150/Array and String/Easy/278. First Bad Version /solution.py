class API:
    def __init__(self, bad_version):
        self.bad_version = bad_version

    def is_bad_version(self, guess: int) -> bool:
        return guess >= self.bad_version


def find_first_bad_version(n: int, api: API) -> int:
    """
    O(log(n)) solution.
    The problem is similar to binary search with duplicated elements.
    """
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if api.is_bad_version(mid):
            right = mid
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    for n in range(1, 5):
        for bad_version in range(1, n):
            api = API(bad_version)
            output = find_first_bad_version(n, api)
            if output != bad_version:
                raise ValueError(f'n={n} version={bad_version} got: {output}')
