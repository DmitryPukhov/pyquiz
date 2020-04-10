from unittest import TestCase

from pyquiz.ctci.sortsearch.SearchInRotatedArray import SearchInRotatedArray


class TestSearchInRotatedArray(TestCase):
    def test_search__with_sorted_array__should_find(self):
        i = SearchInRotatedArray().search(3, [1, 2, 3, 4])
        self.assertEqual(2, i)

    def test_search__with_rotated_array__should_find(self):
        i = SearchInRotatedArray().search(2, [3, 4, 1, 2])
        self.assertEqual(3, i)

    def test_search__with_2elements_array__should_find(self):
        i = SearchInRotatedArray().search(2, [1, 2])
        self.assertEqual(1, i)
        i = SearchInRotatedArray().search(2, [2, 1])
        self.assertEqual(0, i)


    def test_search__with_empty_array__should_be_none(self):
        i = SearchInRotatedArray().search(2, [5, 8, 10])
        self.assertIsNone(i)
