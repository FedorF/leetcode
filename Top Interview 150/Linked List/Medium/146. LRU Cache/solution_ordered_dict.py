from collections import OrderedDict


class LRUCache:
    """
    Apply OrderedDict.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = OrderedDict()

    def is_full(self):
        return len(self.map) == self.capacity

    def get(self, key: int) -> int:
        if key in self.map:
            self.map.move_to_end(key)
            return self.map[key]

        return -1

    def put(self, key: int, value: int):
        if key in self.map:
            self.map[key] = value
            self.map.move_to_end(key)
            return

        if self.is_full():
            self.map.popitem(last=False)

        self.map[key] = value
        return


def run_test(commands, xs):
    """
    Function for testing LRUCache implementation.

    """
    cache = LRUCache(xs[0][0])
    res = []
    for i in range(1, len(commands)):
        res.append(getattr(cache, commands[i])(*xs[i]))

    return res


if __name__ == '__main__':
    commands = ["", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    xs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    actual, expected = run_test(commands, xs), [None, None, 1, None, -1, None, -1, 3, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
