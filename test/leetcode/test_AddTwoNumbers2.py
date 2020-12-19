from unittest import TestCase

from pyquiz.common.ListNode import ListNode
from pyquiz.leetcode.AddTwoNumbers2 import AddTwoNumbers2


class TestAddTwoNumbers2(TestCase):
    def test_add_two_numbers(self):
        """
        Example:
        Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 8 -> 0 -> 7
        """
        res = AddTwoNumbers2().addTwoNumbers(ListNode.of([7, 2, 4, 3]), ListNode.of([5, 6, 4]))
        self.assertEqual("7,8,0,7", str(res))

    def test_add_two_numbers_12_34(self):
        res = AddTwoNumbers2().addTwoNumbers(ListNode.of([1,2]), ListNode.of([3,4]))
        self.assertEqual("4,6", str(res))

    def test_add_two_numbers_12(self):
        res = AddTwoNumbers2().addTwoNumbers(ListNode.of([1]), ListNode.of([2]))
        self.assertEqual("3", str(res))

    def test_add_two_numbers_999_1(self):
        res = AddTwoNumbers2().addTwoNumbers(ListNode.of([9,9,9]), ListNode.of([1]))
        self.assertEqual("1,0,0,0", str(res))
