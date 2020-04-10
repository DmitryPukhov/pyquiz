from unittest import TestCase

from pyquiz.ctci.linkedlists.DeleteMiddleNode import DeleteMiddleNode
from pyquiz.common.ListNode import ListNode


class TestDeleteMiddleNode(TestCase):
    def test_delete_middle_3items(self):
        root = ListNode(0, ListNode(1, ListNode(2, None)))
        DeleteMiddleNode.delete_middle(root.next)
        assert(root.next.val is 2)
