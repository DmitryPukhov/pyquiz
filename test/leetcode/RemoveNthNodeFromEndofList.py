import unittest

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Find last window head
        winhead = head
        wintail = winhead
        for i in range(n):
            wintail = wintail.next

        # Move the window
        winprev = None
        while wintail:
            wintail = wintail.next
            winprev = winhead
            winhead = winhead.next

        # Return old or new head
        if winprev:
            winprev.next = winhead.next
            return head
        else:
            return head.next


class SolutionTest(unittest.TestCase):
    def listof(self, vals: List):
        head = ListNode(vals[0])
        node = head
        for v in vals[1:]:
            node.next = ListNode(v)
            node = node.next
        return head

    def valsof(self, head: ListNode) -> List[int]:
        node = head
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return out

    def test_1234_2(self):
        head = self.listof([1, 2, 3, 4])
        ans = self.valsof(Solution().removeNthFromEnd(head, 2))
        self.assertEqual([1,2,4],ans)

    def test_1234_1(self):
        head = self.listof([1, 2, 3, 4])
        ans = self.valsof(Solution().removeNthFromEnd(head, 1))
        self.assertEqual([1,2,3],ans)

    def test_1234_4(self):
        head = self.listof([1, 2, 3, 4])
        ans = self.valsof(Solution().removeNthFromEnd(head, 4))
        self.assertEqual([2,3,4],ans)

    def test_1_1(self):
        head = self.listof([1])
        ans = self.valsof(Solution().removeNthFromEnd(head, 1))
        self.assertEqual([],ans)

    def test_1_2(self):
        head = self.listof([1])
        ans = self.valsof(Solution().removeNthFromEnd(head, 1))
        self.assertEqual([1],ans)

if __name__ == '__main__':
    unittest.main()
