from unittest import TestCase

from pyzuiz.DeleteMiddleNode import DeleteMiddleNode
from pyzuiz.tools.LinkedListNode import LinkedListNode


class TestDeleteMiddleNode(TestCase):
    def test_delete_middle_3items(self):
        root = LinkedListNode(0, LinkedListNode(1, LinkedListNode(2, None)))
        DeleteMiddleNode.delete_middle(root.next_node)
        assert(root.next_node.value is 2)
