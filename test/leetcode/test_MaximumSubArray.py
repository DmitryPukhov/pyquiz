from unittest import TestCase

from pyzuiz.leetcode.MaximumSubArray import MaximumSubArray


class TestSolution(TestCase):
    def test_max_sub_array(self):
        sum = MaximumSubArray().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
        self.assertEqual(6, sum)
