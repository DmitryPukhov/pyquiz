from unittest import TestCase
from pyquiz.leetcode.FirstMissingPositive import Solution


class TestSolution(TestCase):
    def test_first_missing_positive_example1(self):
        """
        Example 1:
        Input: nums = [1,2,0]
        Output: 3
        """
        self.assertEqual(3, Solution().firstMissingPositive([1, 2, 0]))

    def test_first_missing_positive_example2(self):
        """
        Example 2:
        Input: nums = [3,4,-1,1]
        Output: 2
        """
        self.assertEqual(2, Solution().firstMissingPositive([3, 4, -1, 1]))

    def test_first_missing_positive_example3(self):
        """
        Example 3:
        Input: nums = [7,8,9,11,12]
        Output: 1
        """
        self.assertEqual(1, Solution().firstMissingPositive([7, 8, 9, 11, 12]))

    def test_first_missing_positive_empty(self):
        self.assertEqual(1, Solution().firstMissingPositive([]))

    def test_first_missing_positive_1(self):
        self.assertEqual(2, Solution().firstMissingPositive([1]))

    def test_first_missing_positive_2(self):
        self.assertEqual(1, Solution().firstMissingPositive([2]))


    def test_first_missing_positive_123(self):
        self.assertEqual(4, Solution().firstMissingPositive([1, 2, 3]))

    def test_first_missing_positive_111(self):
        self.assertEqual(2, Solution().firstMissingPositive([1, 1, 1]))

    def test_first_missing_positive_222(self):
        self.assertEqual(1, Solution().firstMissingPositive([2, 2, 2]))

    def test_first_missing_positive_neg1(self):
        self.assertEqual(1, Solution().firstMissingPositive([-1]))

    def test_first_missing_positive_neg1neg2(self):
        self.assertEqual(1, Solution().firstMissingPositive([-1,-2]))

    def test_first_missing_positive_neg11(self):
        self.assertEqual(2, Solution().firstMissingPositive([-1,1]))

    def test_first_missing_positive_0(self):
        self.assertEqual(1, Solution().firstMissingPositive([0]))

    def test_first_missing_positive_01(self):
        self.assertEqual(2, Solution().firstMissingPositive([0,1]))

    def test_first_missing_positive_neg121(self):
        self.assertEqual(3, Solution().firstMissingPositive([-1,2,1]))
