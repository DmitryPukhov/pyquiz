from unittest import TestCase

from pyzuiz.dynamic.MagicIndex import MagicIndex


class TestMagicIndex(TestCase):

    def test_of__with_all_magic_index__should_find_all(self):
        arr = [0, 1, 2, 3]
        mi = MagicIndex().of(arr)
        self.assertListEqual(arr, mi)

    def test_of__with_magic_index__should_find(self):
        arr = [5, 1, 2, 7]
        mi = MagicIndex().of(arr)
        self.assertListEqual([1, 2], mi)

    def test_of__without_magic_index__should_not_find(self):
        arr = [5, 7, 10]
        mi = MagicIndex().of(arr)
        self.assertFalse(None, mi)
