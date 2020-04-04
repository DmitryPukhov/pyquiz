from unittest import TestCase

from pyzuiz.common.SingleLinkedNode import SingleLinkedNode
from pyzuiz.ctci.linkedlists.SumLists import SumLists


class TestSumLists(TestCase):
    def test_sum__with_equal_size(self):
        d1 = SingleLinkedNode.of([3, 2, 1])
        d2 = SingleLinkedNode.of([3, 2, 1])
        res = SumLists().sum_of_reversed(d1, d2)

        self.assertEqual("6,4,2", str(res))

    def test_sum__with_diff_size(self):
        d1 = SingleLinkedNode.of([1])
        d2 = SingleLinkedNode.of([3, 2, 1])
        res = SumLists().sum(d1, d2).str_with_tail()

        self.assertEqual("3,2,2", res)

    def test_sum_of_reversed(self):
        d1 = SingleLinkedNode.of([3, 2, 1])
        d2 = SingleLinkedNode.of([3, 2, 1])
        res = SumLists().sum_of_reversed(d1, d2).str_with_tail()

        self.assertEqual("6,4,2", res)

    def test_sum_of_reversed__with_diff_size(self):
        d1 = SingleLinkedNode.of([1])
        d2 = SingleLinkedNode.of([3, 2, 1])
        res = SumLists().sum_of_reversed(d1, d2).str_with_tail()

        self.assertEqual("4,2,1", res)

    def test_sum_of_reversed__with_carry(self):
        d1 = SingleLinkedNode.of([3])
        d2 = SingleLinkedNode.of([9])
        res = SumLists().sum_of_reversed(d1, d2).str_with_tail()

        self.assertEqual("2,1", res)

    def test_sum_of_reversed(self):
        d1 = SingleLinkedNode.of([3, 2, 1])
        d2 = SingleLinkedNode.of([3, 2, 1])
        res = SumLists().sum_of_reversed(d1, d2).str_with_tail()

        self.assertEqual("6,4,2", res)

    def test_sum_of_reversed_with_carry(self):
        d1 = SingleLinkedNode.of([9])
        d2 = SingleLinkedNode.of([1])
        res = SumLists().sum_of_reversed(d1, d2).str_with_tail()
        self.assertEqual("0,1", res)

        d1 = SingleLinkedNode.of([9, 9, 9])
        d2 = SingleLinkedNode.of([5])
        res = SumLists().sum_of_reversed(d1, d2).str_with_tail()
        self.assertEqual("4,0,0,1", res)

    def test__align__long_list1(self):
        d1 = SingleLinkedNode.of([1, 2, 3])
        d2 = SingleLinkedNode.of([1])
        (res1, res2) = SumLists()._align(d1, d2)

        self.assertEqual("1,2,3", str(res1))
        self.assertEqual("0,0,1", str(res2))

    def test__align__long_list2(self):
        d1 = SingleLinkedNode.of([1])
        d2 = SingleLinkedNode.of([1, 2, 3])
        (res1, res2) = SumLists()._align(d1, d2)

        self.assertEqual("0,0,1", str(res1))
        self.assertEqual("1,2,3", str(res2))

    def test_align__equal_size(self):
        d1 = SingleLinkedNode.of([1])
        d2 = SingleLinkedNode.of([2])
        (res1, res2) = SumLists()._align(d1, d2)
        self.assertEqual("1", str(res1))
        self.assertEqual("2", str(res2))

    def test_align__empty(self):
        d1 = SingleLinkedNode.of([1])
        d2 = SingleLinkedNode.of([2])
        (res1, res2) = SumLists()._align(d1, d2)
        self.assertEqual("1", str(res1))
        self.assertEqual("2", str(res2))

    # def test__pad_left(self):
    #     d1 = SingleLinkedNode.of([1])
    #     res = SumLists()._pad_left(d1, 0, 2)
    #     self.assertEqual("0,0,1", str(res))
