from unittest import TestCase

from pyquiz.algo.sort.QuickSort import QuickSort


class TestQuickSort(TestCase):
    def test_sort__main_case(self):
        res = QuickSort().sort([2, 3, 1, 2, 4])
        self.assertListEqual([1, 2, 2, 3, 4], res)

    def test_sort__empty(self):
        res = QuickSort().sort([])
        self.assertListEqual([], res)

    def test_sort__single(self):
        res = QuickSort().sort([1])
        self.assertListEqual([1], res)

    def test_sort__double(self):
        res = QuickSort().sort([2,1])
        self.assertListEqual([1,2], res)
