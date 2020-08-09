from unittest import TestCase

from pyquiz.common.ListNode import ListNode
from pyquiz.leetcode.PalindromeLinkedList import PalindromeLinkedList


class TestPalindromeLinkedList(TestCase):
    def test_is_palindrome_single(self):
        res = PalindromeLinkedList().isPalindrome(ListNode(1))
        self.assertFalse(res)

    def test_is_palindrome(self):
        res = PalindromeLinkedList().isPalindrome(ListNode(1, ListNode(2)))
        self.assertFalse(res)

        res = PalindromeLinkedList().isPalindrome(ListNode(1, ListNode(2, ListNode(1))))
        self.assertTrue(res)

    def test_reverse(self):
        n = PalindromeLinkedList().reverse(ListNode(1, ListNode(2)))
        self.assertEqual(2, n.val)
        self.assertEqual(1, n.next.val)

    def test_reverse_single(self):
        n = PalindromeLinkedList().reverse(ListNode(1))
        self.assertEqual(1, n.val)

    def test_getlen(self):
        l = PalindromeLinkedList().getlen(ListNode(1, ListNode(2)))
        self.assertEqual(2, l)
