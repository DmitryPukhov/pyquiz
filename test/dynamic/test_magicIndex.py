from unittest import TestCase

from pyzuiz.dynamic.MagicIndex import MagicIndex


class TestMagicIndex(TestCase):

    def test_of_with_multiindex_should_find_multi(self):
        arr = [-1, -2, 2, 3, 4, 4, 6, 7, 8, 10, 11]
        mi = MagicIndex().of(arr)
        self.assertListEqual([(2, 4), (6, 8)], mi)

    def test_of__with_all_magic_index__should_find_all(self):
        arr = [0, 1, 2, 3]
        mi = MagicIndex().of(arr)
        self.assertListEqual([(0, 3)], mi)

    def test_of__with_magic_index__should_find(self):
        arr = [5, 1, 2, 7]
        mi = MagicIndex().of(arr)
        self.assertListEqual([(1, 2)], mi)

    def test_of__without_magic_index__should_not_find(self):
        arr = [5, 7, 10]
        mi = MagicIndex().of(arr)
        self.assertFalse([], mi)

    def test_of_with_single__should_find_single(self):
        arr = [0]
        mi = MagicIndex.of(arr)
        self.assertListEqual([(0,0)], mi)
