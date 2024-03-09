class Node:
    def __init__(self, cnt: int, key: int, next_node: 'Node' = None, prev_node: 'Node' = None):
        self.cnt = cnt
        self.key = key
        self.next_node = next_node
        self.prev_node = prev_node


class LFUCache:
    """
    Least frequently used cache.
    Deletes node that was used the least times.

    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map_val = {}
        self.map_node = {}
        self.lfu = None

    def get(self, key: int) -> int:
        if key in self.map_val:
            node = self.map_node[key]
            node.cnt += 1
            prev = node.prev_node
            nnext = node.next_node
            while nnext and node.cnt > nnext.cnt:
                if prev:
                    prev.next_node = nnext
                else:  # node is a head
                    self.lfu = nnext

                node.next_node, nnext.next_node = nnext.next_node, node
                node.prev_node = nnext
                nnext.prev_node = prev

                if node.next_node:
                    node.next_node.prev_node = node

                prev, nnext = node.prev_node, node.next_node
            return self.map_val[key]

        return -1

    def put(self, key: int, value: int):
        if key in self.map_val:
            self.map_val[key] = value
            return

        if len(self.map_val) < self.capacity:
            self.map_val[key] = value

            node = Node(0, key)
            if not self.lfu:
                self.lfu = node
            else:
                node.next_node = self.lfu
                self.lfu.prev_node = node
                self.lfu = node

            self.map_node[key] = node
            return

        # remove lfu
        key_to_del = self.lfu.key
        self.lfu.key = key
        self.lfu.cnt = 0
        self.map_node.pop(key_to_del)
        self.map_node[key] = self.lfu
        self.map_val.pop(key_to_del)
        self.map_val[key] = value


def run_test(commands, xs):
    """
    Function for testing LFUCache implementation.

    """
    cache = LFUCache(xs[0][0])
    res = []
    for i in range(1, len(commands)):
        res.append(getattr(cache, commands[i])(*xs[i]))

    return res


if __name__ == '__main__':
    commands = ["", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    xs = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    actual, expected = run_test(commands, xs), [None, None, 1, None, -1, None, 1, -1, 4]
    assert actual == expected, f"expected: {expected}, actual: {actual}"
