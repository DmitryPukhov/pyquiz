from unittest import TestCase

from pyzuiz.common.SingleLinkedNode import SingleLinkedNode
from pyzuiz.linkedlists.SumLists import SumLists


class TestSumLists(TestCase):

    def test_sum(self):
        d1 = SingleLinkedNode.of([3, 2, 1])
        d2 = SingleLinkedNode.of([3, 2, 1])
        res = SumLists().sum(d1, d2).str_with_tail()

        self.assertEqual("6,4,2", res)

    def test_sum_carry(self):
        d1 = SingleLinkedNode.of([9])
        d2 = SingleLinkedNode.of([1])
        res = SumLists().sum(d1, d2).str_with_tail()
        self.assertEqual("0,1", res)

        d1 = SingleLinkedNode.of([9, 9, 9])
        d2 = SingleLinkedNode.of([5])
        res = SumLists().sum(d1, d2).str_with_tail()
        self.assertEqual("4,0,0,1", res)
