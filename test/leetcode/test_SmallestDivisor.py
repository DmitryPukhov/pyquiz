from unittest import TestCase
from pyquiz.leetcode.SmallestDivisor import Solution


class TestSolution(TestCase):

    def test_smallest_divisor__example1(self):
        """
        Example 1:
        Input: nums = [1,2,5,9], threshold = 6
        Output: 5
        Explanation: We can get a sum to 17 (1+2+5+9) if the divisor is 1.
        If the divisor is 4 we can get a sum of 7 (1+1+2+3) and if the divisor is 5 the sum will be 5 (1+1+1+2).
        """
        self.assertEqual(5, Solution().smallestDivisor(nums=[1, 2, 5, 9], threshold=6))

    def test_smallest_divisor__example2(self):
        """
        Example 2:
        Input: nums = [44,22,33,11,1], threshold = 5
        Output: 44
        """
        self.assertEqual(44, Solution().smallestDivisor(nums=[44, 22, 33, 11, 1], threshold=5))

    def test_smallest_divisor__example3(self):
        """
        Example 3:
        Input: nums = [21212,10101,12121], threshold = 1000000
        Output: 1
        """
        self.assertEqual(1, Solution().smallestDivisor(nums=[21212, 10101, 12121], threshold=1000000))

    def test_smallest_divisor__example4(self):
        """
        Example 4:
        Input: nums = [2,3,5,7,11], threshold = 11
        Output: 3
        """
        self.assertEqual(3, Solution().smallestDivisor(nums=[2, 3, 5, 7, 11], threshold=11))

    def test_smallest_divisor__1__1(self):
        self.assertEqual(1, Solution().smallestDivisor(nums=[1], threshold=1))
