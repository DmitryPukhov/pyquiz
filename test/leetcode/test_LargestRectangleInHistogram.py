from unittest import TestCase

from pyquiz.leetcode.LargestRectangleInHistogram import Solution


class TestSolution(TestCase):

    def test_largest_rectangle_area__example1(self):
        """
       Example 1:
       Input: heights = [2,1,5,6,2,3]
       Output: 10
       Explanation: The above is a histogram where width of each bar is 1.
       The largest rectangle is shown in the red area, which has an area = 10 units.
        """
        out = Solution().largestRectangleArea([2, 1, 5, 6, 2, 3])
        self.assertEqual(10, out)

    def test_largest_rectangle_area__example2(self):
        """
        Input: [2,4]
        Output: 4
        """
        out = Solution().largestRectangleArea([2, 4])
        self.assertEqual(4, out)

    def test_largest_rectangle_area__0(self):
        out = Solution().largestRectangleArea([0])
        self.assertEqual(0, out)

    def test_largest_rectangle_area__1(self):
        out = Solution().largestRectangleArea([1])
        self.assertEqual(1, out)

    def test_largest_rectangle_area__empty(self):
        out = Solution().largestRectangleArea([])
        self.assertEqual(0, out)

    def test_largest_rectangle_area__2121(self):
        out = Solution().largestRectangleArea([2, 1, 2, 1])
        self.assertEqual(4, out)
