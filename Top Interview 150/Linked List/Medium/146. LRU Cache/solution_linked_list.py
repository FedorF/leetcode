class Node:
    """
    Double linked-list implementation
    """

    def __init__(self, key: int, value: int, next_node: 'Node' = None, prev_node: 'Node' = None):
        self.key = key
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node


class LRUCache:
    """
    Apply double linked-list.

    The head node of list is an LRU, and tail node is a most frequently used key.
    For example,

    head                         tail
      1  ->  2  ->  3  ->  4  ->  5

    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = None
        self.tail = None

    def is_full(self):
        return len(self.map) == self.capacity

    def move_to_tail(self, key: int):
        node = self.map[key]
        if node == self.tail:
            return

        if node == self.head:
            if len(self.map) == 1:
                return

            next_node = node.next_node
            next_node.prev_node = None
            self.head = next_node

            old_tail = self.tail
            old_tail.next_node = node
            node.prev_node = old_tail
            self.tail = node
            return

        if not self.head:  # no nodes
            self.head = node
            self.head.next_node = None
            self.head.prev_node = None
            return

        if not self.tail:  # one node
            self.tail = node
            self.tail.next_node = None
            self.tail.prev_node = self.head
            self.head.next_node = self.tail
            return

        if not node.prev_node and not node.next_node:
            old_tail = self.tail
            old_tail.next_node = node
            node.prev_node = old_tail
            self.tail = node
            return

        prev_node, next_node = node.prev_node, node.next_node
        prev_node.next_node = next_node
        next_node.prev_node = prev_node
        old_tail = self.tail
        old_tail.next_node = node
        node.prev_node = old_tail
        self.tail = node
        return

    def get(self, key: int) -> int:
        if key in self.map:
            self.move_to_tail(key)
            return self.map[key].value

        return -1

    def put(self, key: int, value: int):
        if key in self.map:
            self.move_to_tail(key)
            self.map[key].value = value
            return

        if self.is_full():
            self.map.pop(self.head.key)  # remove lru
            head_next = self.head.next_node
            self.head = Node(key, value)
            self.head.next_node = head_next
            self.map[key] = self.head
            self.move_to_tail(key)
            return

        self.map[key] = Node(key, value)
        self.move_to_tail(key)
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
