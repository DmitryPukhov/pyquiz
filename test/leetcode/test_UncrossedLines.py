from unittest import TestCase
from pyquiz.leetcode.UncrossedLines import Solution


class TestSolution(TestCase):
    def test_max_uncrossed_lines__example1(self):
        """
        Example 1:
        Input: A = [1,4,2], B = [1,2,4]
        Output: 2
        Explanation: We can draw 2 uncrossed lines as in the diagram.
        We cannot draw 3 uncrossed lines, because the line from A[1]=4 to B[2]=4
        will intersect the line from A[2]=2 to B[1]=2.
        """
        self.assertEqual(2, Solution().maxUncrossedLines(A=[1, 4, 2], B=[1, 2, 4]))

    def test_max_uncrossed_lines__example2(self):
        """
         Example 2:
        Input: A = [2,5,1,2,5], B = [10,5,2,1,5,2]
        Output: 3
        """
        self.assertEqual(3, Solution().maxUncrossedLines(A=[2, 5, 1, 2, 5], B=[10, 5, 2, 1, 5, 2]))

    def test_max_uncrossed_lines__example3(self):
        """
        Example 3:
        Input: A = [1,3,7,1,7,5], B = [1,9,2,5,1]
        Output: 2        """
        self.assertEqual(2, Solution().maxUncrossedLines(A=[1, 3, 7, 1, 7, 5], B=[1, 9, 2, 5, 1]))

    def test_max_uncrossed_lines__large(self):
        self.assertIsNotNone(Solution().maxUncrossedLines(
            A=[1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7,
               5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1,
               7, 5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7, 5, 1, 3, 7, 1, 7, 5],
            B=[1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1,
               1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1,
               1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1, 1, 9, 2, 5, 1]))

    def test_max_uncrossed_lines__1_1etc(self):
        self.assertEqual(1, Solution().maxUncrossedLines(A=[1], B=[1, 2, 3]))

    def test_max_uncrossed_lines__1_not1etc(self):
        self.assertEqual(0, Solution().maxUncrossedLines(A=[1], B=[4, 2, 3]))
