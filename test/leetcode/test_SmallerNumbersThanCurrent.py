from unittest import TestCase

from pyquiz.leetcode.SmallerNumbersThanCurrent import SmallerNumbersThanCurrent


class TestSmallerNumbersThanCurrent(TestCase):
    alg = SmallerNumbersThanCurrent()

    def test_smaller_numbers_than_current(self):
        self.assertListEqual([2, 1, 0, 3], self.alg.smaller_numbers_than_current([6, 5, 4, 8]))
