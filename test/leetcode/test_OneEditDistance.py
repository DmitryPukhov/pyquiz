from unittest import TestCase
from pyquiz.leetcode.OneEditDistance import Solution


class TestSolution(TestCase):
    def test_is_one_edit_distance__example1(self):
        """
        Example 1:
        Input: s = "ab", t = "acb"
        Output: true
        Explanation: We can insert 'c' into s to get t.
        """
        self.assertTrue(Solution().isOneEditDistance(s="ab", t="acb"))

    def test_is_one_edit_distance__example2(self):
        """
        Example 2:
        Input: s = "", t = ""
        Output: false
        Explanation: We cannot get t from s by only one step.
        """
        self.assertFalse(Solution().isOneEditDistance(s="", t=""))

    def test_is_one_edit_distance__example3(self):
        """
        Example 3:
        Input: s = "a", t = ""
        Output: true
        """
        self.assertTrue(Solution().isOneEditDistance(s="a", t=""))

    def test_is_one_edit_distance__example4(self):
        """
        Example 4:
        Input: s = "", t = "A"
        Output: true
        """
        self.assertTrue(Solution().isOneEditDistance(s="", t="A"))

    def test_is_one_edit_distance__a_a(self):
        self.assertFalse(Solution().isOneEditDistance(s="a", t="a"))
