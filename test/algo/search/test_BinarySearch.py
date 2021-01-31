from unittest import TestCase

from pyquiz.algo.search.BinarySearch import BinarySearch


class TestBinarySearch(TestCase):

    def test_find_ge_124_1(self):
        self.assertEqual(1, BinarySearch().find_ge([1, 2, 4], 1))

    def test_find_ge_124_4(self):
        self.assertEqual(4, BinarySearch().find_ge([1, 2, 4], 4))

    def test_find_ge_124_3(self):
        self.assertEqual(4, BinarySearch().find_ge([1, 2, 4], 3))

    def test_find_greater_124_0(self):
        self.assertEqual(1, BinarySearch().find_greater([1, 2, 4], 0))

    def test_find_greater_124_4(self):
        self.assertEqual(None, BinarySearch().find_greater([1, 2, 4], 4))

    def test_find_greater_124_3(self):
        self.assertEqual(4, BinarySearch().find_greater([1, 2, 4], 3))

    def test_find_less_124_1(self):
        self.assertIsNone(BinarySearch().find_less([1, 2, 4], 1))

    def test_find_less_124_3(self):
        self.assertEqual(2, BinarySearch().find_less([1, 2, 4], 3))

    def test_find_less_124_2(self):
        self.assertEqual(1, BinarySearch().find_less([1, 2, 4], 2))

    def test_find_less_124_1(self):
        self.assertIsNone(BinarySearch().find_less([1, 2, 4], 1))

    def test_find_le_124_3(self):
        self.assertEqual(2, BinarySearch().find_le([1, 2, 4], 3))

    def test_find_le_124_2(self):
        self.assertEqual(2, BinarySearch().find_le([1, 2, 4], 2))

    def test_find_le_124_1(self):
        self.assertEqual(1, BinarySearch().find_le([1, 2, 4], 1))

    def test_find_124_4(self):
        self.assertEqual(2, BinarySearch().find_index([1, 2, 4], 4))

    def test_find_124_5(self):
        self.assertEqual(-1, BinarySearch().find_index([1, 2, 4], 5))

    def test_find_124_0(self):
        self.assertEqual(-1, BinarySearch().find_index([1, 2, 4], 0))

    def test_find_1_1(self):
        self.assertEqual(0, BinarySearch().find_index([1], 1))

    def test_find_1_0(self):
        self.assertEqual(-1, BinarySearch().find_index([1], 0))

    def test_find_1_2(self):
        self.assertEqual(-1, BinarySearch().find_index([1], 2))

    def test_find_12_1(self):
        self.assertEqual(0, BinarySearch().find_index([1,2], 1))

    def test_find_12_2(self):
        self.assertEqual(1, BinarySearch().find_index([1,2], 2))

    def test_find_12_0(self):
        self.assertEqual(-1, BinarySearch().find_index([1,2], 0))

    def test_find_12_3(self):
        self.assertEqual(-1, BinarySearch().find_index([1,2], 3))

    def test_find_empty_items(self):
        self.assertEqual(-1, BinarySearch().find_index([], 3))

    def test_find_empty_val(self):
        self.assertEqual(-1, BinarySearch().find_index([1], None))

    def test_find_empty_items_and_val(self):
        self.assertEqual(-1, BinarySearch().find_index([], None))
