from unittest import TestCase

from pyzuiz.algo.MergeSort import MergeSort


class TestMergeSort(TestCase):
    def test_sort__main_case(self):
        res = MergeSort().sort([2, 3, 1, 2, 4])
        self.assertListEqual([1, 2, 2, 3, 4], res)

    def test_sort__empty(self):
        res = MergeSort().sort([])
        self.assertListEqual([], res)

    def test_sort__single(self):
        res = MergeSort().sort([1])
        self.assertListEqual([1], res)

    # def test_split(self):
    #     self.fail()
    #
    # def test_merge(self):
    #     self.fail()
