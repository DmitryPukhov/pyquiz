from unittest import TestCase
from pyquiz.leetcode.FibonacciNumber import Solution


class TestSolution(TestCase):

    def test_fib_example1(self):
        """
        Example 1:

        Input: n = 2
        Output: 1
        Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
        """
        out = Solution().fib(2)
        self.assertEqual(1, out)

    def test_fib_example2(self):
        """
        Example 2:
        Input: n = 3
        Output: 2
        Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
        """
        out = Solution().fib(3)
        self.assertEqual(2, out)

    def test_fib_example3(self):
        """
        Example 3:
        Input: n = 4
        Output: 3
        Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
        """
        out = Solution().fib(4)
        self.assertEqual(3, out)
