from unittest import TestCase
from pyquiz.leetcode.FindDuplicate import Solution


class TestSolution(TestCase):

    def test_find_duplicate_example1(self):
        """
        Example 1:
        Input: nums = [1,3,4,2,2]
        Output: 2
        """
        self.assertEqual(2, Solution().findDuplicate(nums=[1, 3, 4, 2, 2]))

    def test_find_duplicate_example2(self):
        """
        Example 2:
        Input: nums = [3,1,3,4,2]
        Output: 3
        """
        self.assertEqual(3, Solution().findDuplicate(nums=[3, 1, 3, 4, 2]))

    def test_find_duplicate_example3(self):
        """
        Example 3:
        Input: nums = [1,1]
        Output: 1
        """
        self.assertEqual(1, Solution().findDuplicate(nums=[1, 1]))

    def test_find_duplicate_example4(self):
        """
        Example 4:
        Input: nums = [1,1,2]
        Output: 1
        """
        self.assertEqual(1, Solution().findDuplicate(nums=[1, 1, 2]))
