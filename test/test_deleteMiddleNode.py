from unittest import TestCase

from pyzuiz.DeleteMiddleNode import DeleteMiddleNode
from pyzuiz.tools.SingleLinkedNode import SingleLinkedNode


class TestDeleteMiddleNode(TestCase):
    def test_delete_middle_3items(self):
        root = SingleLinkedNode(0, SingleLinkedNode(1, SingleLinkedNode(2, None)))
        DeleteMiddleNode.delete_middle(root.next_)
        assert(root.next_.value is 2)
