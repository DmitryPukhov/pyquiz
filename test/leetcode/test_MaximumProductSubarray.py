from unittest import TestCase

from pyquiz.leetcode.MaximumProductSubarray import MaximumProductSubarray


class TestMaximumProductSubarray(TestCase):
    def test_max_product_example1(self):
        """
        Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

        Example 1:
        Input: [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.

        Example 2:
        Input: [-2,0,-1]
        Output: 0
        Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
        """

        res = MaximumProductSubarray().maxProduct([2, 3, -2, 4])
        self.assertEqual(6, res)

    def test_max_product_example2(self):
        """
        Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

        Example 1:
        Input: [2,3,-2,4]
        Output: 6
        Explanation: [2,3] has the largest product 6.

        Example 2:
        Input: [-2,0,-1]
        Output: 0
        Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
        """

        res = MaximumProductSubarray().maxProduct([-2, 0, -1])
        self.assertEqual(0, res)

    def test_max_product_2neg3neg2(self):
        res = MaximumProductSubarray().maxProduct([2,-3,-2])
        self.assertEqual(12, res)

    def test_max_product_2neg3(self):
        res = MaximumProductSubarray().maxProduct([2,-3])
        self.assertEqual(2, res)


    def test_max_product_2neg3neg5(self):
        res = MaximumProductSubarray().maxProduct([-2,-3,-5 ])
        self.assertEqual(15, res)