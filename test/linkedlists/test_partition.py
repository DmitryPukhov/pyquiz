from unittest import TestCase

from pyzuiz.common.SingleLinkedNode import SingleLinkedNode
from pyzuiz.linkedlists.Partition import Partition


class TestPartition(TestCase):

    def test_partition(self):
        head = SingleLinkedNode(1,
                                SingleLinkedNode(2,
                                                 SingleLinkedNode(3, None)))
        partitioned = Partition().partition(head, 2)

        self.assertListEqual([1, 2, 3], self.as_array(partitioned))

    @staticmethod
    def as_array(node: SingleLinkedNode):
        arr = []
        while node is not None:
            arr.append(node.value)
            node = node.next
        return arr
