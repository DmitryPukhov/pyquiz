from unittest import TestCase

from pyquiz.leetcode.FindDuplicates import FindDuplicates


class TestFindDuplicates(TestCase):
    def test_find_duplicates__example(self):
        """
        Example:
        Input:
        [4,3,2,7,8,2,3,1]

        Output:
        [2,3]
        """
        self.assertEqual([2, 3], FindDuplicates().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))

    def test_find_duplicates__1(self):
        self.assertEqual([], FindDuplicates().findDuplicates([1]))

    def test_find_duplicates__1_1(self):
        self.assertEqual([1], FindDuplicates().findDuplicates([1, 1]))

    def test_find_duplicates__1_2_1(self):
        self.assertEqual([1], FindDuplicates().findDuplicates([1, 2, 1]))

    def test_find_duplicates__1_1_2(self):
        self.assertEqual([1], FindDuplicates().findDuplicates([1, 1, 2]))

    def test_find_duplicates__2_1_1(self):
        self.assertEqual([1], FindDuplicates().findDuplicates([2, 1, 1]))
