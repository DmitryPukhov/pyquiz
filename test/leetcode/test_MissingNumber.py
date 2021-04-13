from unittest import TestCase
from pyquiz.leetcode.MissingNumber import Solution


class TestSolution(TestCase):
    def test_missing_number__example1(self):
        """
        Example 1:
        Input: nums = [3,0,1]
        Output: 2
        Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
         """
        self.assertEqual(2, Solution().missingNumber(nums=[3, 0, 1]))

    def test_missing_number__example2(self):
        """
        Example 2:
        Input: nums = [0,1]
        Output: 2
        Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
        """
        self.assertEqual(2, Solution().missingNumber(nums = [0,1]))

    def test_missing_number__example3(self):
        """
        Example 3:
        Input: nums = [9,6,4,2,3,5,7,0,1]
        Output: 8
        Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
        """
        self.assertEqual(8, Solution().missingNumber(nums=[9, 6, 4, 2, 3, 5, 7, 0, 1]))

    def test_missing_number__example4(self):
        """
        Example 4:
        Input: nums = [0]
        Output: 1
        Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.
        """
        self.assertEqual(1, Solution().missingNumber(nums=[0]))

    def test_missing_number__1(self):
        self.assertEqual(0, Solution().missingNumber(nums=[1]))
