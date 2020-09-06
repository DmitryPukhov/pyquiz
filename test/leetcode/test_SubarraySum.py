from unittest import TestCase

from pyquiz.leetcode.SubarraySum import SubarraySum


class TestSubarraySum(TestCase):
    def test_subarray_sum__empty(self):
        self.assertEqual(0, SubarraySum().subarraySum([], 0))
        self.assertEqual(0, SubarraySum().subarraySum(None, 0))

    def test_subarray_sum__singleinput(self):
        self.assertEqual(1, SubarraySum().subarraySum([1], 1))
        self.assertEqual(0, SubarraySum().subarraySum([1], -1))

    def test_subarray_sum__samevalue(self):
        self.assertEqual(2, SubarraySum().subarraySum([1, 1, 1], 2))
        self.assertEqual(3, SubarraySum().subarraySum([1, 1, 1], 1))

    def test_subarray_sum__singlevalue(self):
        self.assertEqual(1, SubarraySum().subarraySum([1, 2, 1], 2))

