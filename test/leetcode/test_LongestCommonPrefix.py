from unittest import TestCase

from pyquiz.leetcode.LongestCommonPrefix import LongestCommonPrefix


class TestLongestCommonPrefix(TestCase):
    alg = LongestCommonPrefix()

    def test_longest_common_prefix__with_prefix(self):
        self.assertEqual("ab", self.alg.longestCommonPrefix(list(["abc", "abde", "abcccccc"])))
        self.assertEqual("ab", self.alg.longestCommonPrefix(list(["abc", "abce", "abdccccc"])))

    def test_longest_common_prefix__no_prefix(self):
        self.assertEqual("", self.alg.longestCommonPrefix(list(["cbc", "abce", "abdccccc"])))

    def test_longest_common_prefix__empty_strings(self):
        self.assertEqual("", self.alg.longestCommonPrefix(list(["", "a", "ab"])))
        self.assertEqual("", self.alg.longestCommonPrefix(list(["", "", ""])))
        self.assertEqual("", self.alg.longestCommonPrefix(list([None, None, None])))
        self.assertEqual("", self.alg.longestCommonPrefix(list(["abc", None, None])))
        self.assertEqual("", self.alg.longestCommonPrefix(list(["abc", "", None])))
        self.assertEqual("", self.alg.longestCommonPrefix(list([None, "a", None])))

    def test_longest_common_prefix__singe_strings(self):
        self.assertEqual("a", self.alg.longestCommonPrefix(list(["a", "a"])))
        self.assertEqual("a", self.alg.longestCommonPrefix(list(["a"])))
