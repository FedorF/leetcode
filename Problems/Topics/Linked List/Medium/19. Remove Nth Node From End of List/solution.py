class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        lenght = -1
        cur = ListNode(-1, head)
        while cur:
            lenght += 1
            cur = cur.next

        if lenght - n == 0:
            return head.next

        cur = ListNode(-1, head)
        for i in range(lenght - n):
            cur = cur.next

        cur.next = cur.next.next
        return head


if __name__ == '__main__':
    pass
    # todo: tests
