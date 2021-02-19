from unittest import TestCase
from pyquiz.leetcode.MinWindowSubstring import Solution


class TestSolution(TestCase):
    def test_min_window__example1(self):
        """
        Example 1:
        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        """
        self.assertEqual("BANC", Solution().minWindow(s="ADOBECODEBANC", t="ABC"))

    def test_min_window__example2(self):
        """
        Example 2:
        Input: s = "a", t = "a"
        Output: "a"
        """
        self.assertEqual("a", Solution().minWindow(s="a", t="a"))

    def test_min_window__abcd_bc(self):
        self.assertEqual("bc", Solution().minWindow(s="abcd", t="bc"))

    def test_min_window__abc_ab(self):
        self.assertEqual("ab", Solution().minWindow(s="abc", t="ab"))

    def test_min_window__abc_ab(self):
        self.assertEqual("bc", Solution().minWindow(s="bc", t="bc"))

    def test_min_window__abac(self):
        self.assertEqual("cba", Solution().minWindow(s="antcbanc", t="abc"))

    def test_min_window__aabbcc_abbc(self):
        self.assertEqual("", Solution().minWindow(s="aabbcc", t="abbbc"))

    def test_min_window__aabbcc_c(self):
        self.assertEqual("c", Solution().minWindow(s="aabbcc", t="c"))

    def test_min_window__abcd_a(self):
        self.assertEqual("a", Solution().minWindow(s="abcd", t="a"))

    def test_min_window__abcd_d(self):
        self.assertEqual("d", Solution().minWindow(s="abcd", t="d"))

    def test_min_window__abcd_e(self):
        self.assertEqual("", Solution().minWindow(s="abcd", t="e"))

    def test_min_window__abbbcdddddabbcdddddddabc_cba(self):
        self.assertEqual("abc", Solution().minWindow(s="abbbcdddddabbcdddddddabc", t="cba"))

    def test_min_window__aabcd_ab(self):
        self.assertEqual("ab", Solution().minWindow(s="aabcd", t="ab"))

    def test_min_window__aabccd_bc(self):
        self.assertEqual("bc", Solution().minWindow(s="aabccd", t="bc"))
