from unittest import TestCase
from pyquiz.leetcode.RegularExpressionMatching import Solution


class TestSolution(TestCase):
    def test_is_match__example1(self):
        """
        Example 1:
        Input: s = "aa", p = "a"
        Output: false
        Explanation: "a" does not match the entire string "aa".
        """
        self.assertFalse(Solution().isMatch(s="aa", p="a"))

    def test_is_match__example2(self):
        """
        Example 2:
        Input: s = "aa", p = "a*"
        Output: true
        Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
        """
        self.assertTrue(Solution().isMatch(s="aa", p="a*"))

    def test_is_match__example3(self):
        """
        Example 3:
        Input: s = "ab", p = ".*"
        Output: true
        Explanation: ".*" means "zero or more (*) of any character (.)".
        """
        self.assertTrue(Solution().isMatch(s="ab", p=".*"))

    def test_is_match__example4(self):
        """
        Example 4:
        Input: s = "aab", p = "c*a*b"
        Output: true
        Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
        """
        self.assertTrue(Solution().isMatch(s="aab", p="c*a*b"))

    def test_is_match__example5(self):
        """
        Example 5:
        Input: s = "mississippi", p = "mis*is*p*."
        Output: false
        """
        self.assertFalse(Solution().isMatch("mississippi", p="mis*is*p*."))

    def test_is_match__ab_dotmany(self):
        self.assertTrue(Solution().isMatch("ab", p=".*"))

    def test_is_match__abc_dotmanyc(self):
        self.assertTrue(Solution().isMatch("abc", p=".*c"))

    def test_is_match__abc_dotmanyd(self):
        self.assertFalse(Solution().isMatch("abc", p=".*d"))

    def test_is_match__acb_dotmanybmany(self):
        self.assertTrue(Solution().isMatch("accb", p=".*b*"))

    def test_is_match__a_dotmanydotmany(self):
        self.assertTrue(Solution().isMatch("a", p=".*.*"))

    def test_is_match__ab_amanydot(self):
        self.assertTrue(Solution().isMatch("a", p=".*."))

    def test_is_match__abc_amanydot(self):
        """
        Example 5:
        Input: s = "mississippi", p = "mis*is*p*."
        Output: false
        """
        self.assertFalse(Solution().isMatch("abc", p="a*."))

    def test_is_match_a_abmany(self):
        self.assertTrue(Solution().isMatch("a", p="ab*"))
