from unittest import TestCase
from pyquiz.leetcode.WildcardMatching import Solution


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
        Input: s = "aa", p = "*"
        Output: true
        Explanation: '*' matches any sequence.
        """
        self.assertTrue(Solution().isMatch(s="aa", p="*"))

    def test_is_match__example3(self):
        """
        Example 3:
        Input: s = "cb", p = "?a"
        Output: false
        Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
        """
        self.assertFalse(Solution().isMatch(s = "cb", p = "?a"))

    def test_is_match__example4(self):
        """
        Example 4:
        Input: s = "adceb", p = "*a*b"
        Output: true
        Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
        """
        self.assertTrue(Solution().isMatch(s = "adceb", p = "*a*b"))

    def test_is_match__example5(self):
        """
        Example 5:
        Input: s = "acdcb", p = "a*c?b"
        Output: false
        """
        self.assertFalse(Solution().isMatch(s = "acdcb", p = "a*c?b"))

    def test_is_match__abcd_keenysinglekeenysingle(self):
        self.assertTrue(Solution().isMatch(s = "abcd", p = "*?*?"))

    def test_is_match__a_keeny_keeny(self):
        self.assertTrue(Solution().isMatch(s = "a", p = "**"))

    def test_is_match__empty_keeny_keeny(self):
        self.assertTrue(Solution().isMatch(s = "", p = "**"))

    def test_is_match__sempty_pempty(self):
        self.assertTrue(Solution().isMatch(s = "", p = ""))

    def test_is_match__snone_pnone(self):
        self.assertTrue(Solution().isMatch(s = None, p = None))

    def test_is_match__a_empty(self):
        self.assertFalse(Solution().isMatch(s = "a", p = ""))

    def test_is_match__longs(self):
        Solution().isMatch("babaaababaabababbbbbbaabaabbabababbaababbaaabbbaaab","***bba**a*bbba**aab**b")
