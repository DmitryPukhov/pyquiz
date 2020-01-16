from unittest import TestCase

from pyzuiz.ctci.dynamic.MagicIndex import MagicIndex


class TestMagicIndex(TestCase):

    def test_single_with_index_should_find(self):
        arr = [-1, 1, 2, 4]
        start, end = MagicIndex().single(arr)
        self.assertEqual((start, end), (1, 2))

    def test_single_no_index__should_not_find(self):
        arr = [3, 4]
        res = MagicIndex().single(arr)
        self.assertIsNone(res)

    def test_single__with_one_element__should_find(self):
        arr = [0]
        start, end = MagicIndex().single(arr)
        self.assertEqual((0, 0), (start, end))

    def test_multi_with_multi_index_should_find_multi(self):
        arr = [-1, -2, 2, 3, 4, 4, 6, 7, 8, 10, 11]
        mi = MagicIndex().multi(arr)
        self.assertListEqual([(2, 4), (6, 8)], mi)

    def test_multi__with_all_magic_index__should_find_all(self):
        arr = [0, 1, 2, 3]
        mi = MagicIndex().multi(arr)
        self.assertListEqual([(0, 3)], mi)

    def test_multi__with_magic_index__should_find(self):
        arr = [5, 1, 2, 7]
        mi = MagicIndex().multi(arr)
        self.assertListEqual([(1, 2)], mi)

    def test_multi__without_magic_index__should_not_find(self):
        arr = [5, 7, 10]
        mi = MagicIndex().multi(arr)
        self.assertFalse([], mi)

    def test_multi_with_single__should_find_single(self):
        arr = [0]
        mi = MagicIndex.multi(arr)
        self.assertListEqual([(0, 0)], mi)
