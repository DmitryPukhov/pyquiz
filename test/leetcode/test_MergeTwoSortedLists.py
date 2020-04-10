from unittest import TestCase

from pyquiz.common.ListNode import ListNode
from pyquiz.leetcode.MergeTwoSortedLists import MergeTwoSortedLists


class TestMergeTwoSortedLists(TestCase):
    alg = MergeTwoSortedLists()

    def test_merge_two_lists__same_len(self):
        # Init
        l1 = ListNode.of([1, 3, 5])
        l2 = ListNode.of([2, 4, 6])

        # Call and check
        l3 = self.alg.mergeTwoLists(l1, l2).str_with_tail()
        self.assertEqual('1,2,3,4,5,6', l3)

        l3 = self.alg.mergeTwoLists(l2, l1).str_with_tail()
        self.assertEqual('1,2,3,4,5,6', l3)

    def test_merge_two_lists__diff_len(self):
        # Init
        l1 = ListNode.of([1, 2, 5, 6])
        l2 = ListNode.of([3, 4])

        # Call and check
        l3 = self.alg.mergeTwoLists(l1, l2).str_with_tail()
        self.assertEqual('1,2,3,4,5,6', l3)
        # Call and check
        l3 = self.alg.mergeTwoLists(l2, l1).str_with_tail()
        self.assertEqual('1,2,3,4,5,6', l3)

    def test_merge_two_lists__one_empty(self):
        # Init
        l1 = ListNode.of([])
        l2 = ListNode.of([1, 3, 4, 10])
        # Call and check
        l3 = self.alg.mergeTwoLists(l1, l2).str_with_tail()
        self.assertEqual('1,3,4,10', l3)

        l2 = ListNode.of([])
        l1 = ListNode.of([1, 3, 4, 10])
        # Call and check
        l3 = self.alg.mergeTwoLists(l1, l2).str_with_tail()
        self.assertEqual('1,3,4,10', l3)
