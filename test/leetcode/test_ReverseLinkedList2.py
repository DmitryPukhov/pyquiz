from unittest import TestCase

from pyquiz.common.ListNode import ListNode
from pyquiz.leetcode.ReverseLinkedList2 import ReverseLinkedList2


class TestReverseLinkedList2(TestCase):

    def test_reverse_between__example1(self):
        """
        Example:
        Input: 1->2->3->4->5->NULL, m = 2, n = 4
        Output: 1->4->3->2->5->NULL
        """
        res = ReverseLinkedList2().reverseBetween(head=ListNode.of([1, 2, 3, 4, 5]), m=2, n=4)
        self.assertEqual("1,4,3,2,5", str(res))

    def test_reverse_between__emptyleft(self):
        res = ReverseLinkedList2().reverseBetween(head=ListNode.of([1, 2, 3, 4, 5]), m=1, n=2)
        self.assertEqual("2,1,3,4,5", str(res))

    def test_reverse_between__emptyright(self):
        res = ReverseLinkedList2().reverseBetween(head=ListNode.of([1, 2, 3, 4, 5]), m=4, n=5)
        self.assertEqual("1,2,3,5,4", str(res))

    def test_reverse_between__12345_1_1(self):
        res = ReverseLinkedList2().reverseBetween(head=ListNode.of([1, 2, 3, 4, 5]), m=1, n=1)
        self.assertEqual("1,2,3,4,5", str(res))

    def test_reverse_between__12345_5_5(self):
        res = ReverseLinkedList2().reverseBetween(head=ListNode.of([1, 2, 3, 4, 5]), m=5, n=5)
        self.assertEqual("1,2,3,4,5", str(res))

    def test_reverse_between__15(self):
        res = ReverseLinkedList2().reverseBetween(head=ListNode.of([1]), m=1, n=1)
        self.assertEqual("1", str(res))
