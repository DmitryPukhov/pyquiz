from unittest import TestCase

from pyquiz.leetcode.LastSubstring import LastSubstring


class TestLastSubstring(TestCase):
    def test_last_substring__example1(self):
        """
        Example 1:
        Input: "abab"
        Output: "bab"
        Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".
        """
        ss = LastSubstring().lastSubstring("abab")
        self.assertEqual("bab", ss)

    def test_last_substring__example2(self):
        """
        Example 2:
        Input: "leetcode"
        Output: "tcode"
        """
        ss = LastSubstring().lastSubstring("leetcode")
        self.assertEqual("tcode", ss)

    def test_last_substring__a(self):
        ss = LastSubstring().lastSubstring("a")
        self.assertEqual("a", ss)

    def test_last_substring__ab(self):
        ss = LastSubstring().lastSubstring("ab")
        self.assertEqual("b", ss)

    def test_last_substring__wewi(self):
        ss = LastSubstring().lastSubstring("wewicidewidic")
        self.assertEqual("widic", ss)

    def test_last_substring__a100k(self):
        s = ''.join(["a"]*(10**6))
        ss = LastSubstring().lastSubstring(s)
        self.assertEqual(s,ss)