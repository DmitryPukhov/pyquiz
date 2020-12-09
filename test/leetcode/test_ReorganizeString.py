from unittest import TestCase

from pyquiz.leetcode.ReorganizeString import ReorganizeString


class TestReorganizeString(TestCase):

    def test_reorganize_string__example1(self):
        """
        Example 1:
        Input: S = "aab"
        Output: "aba"
        """
        self.assertEqual("aba", ReorganizeString().reorganizeString("aab"))

    def test_reorganize_string__example2(self):
        """
        Example 2:
        Input: S = "aaab"
        Output: ""
        """
        self.assertEqual("", ReorganizeString().reorganizeString("aaab"))

    def test_reorganize_string__aabbcc(self):
        self.assertEqual("bacacb", ReorganizeString().reorganizeString("aabbcc"))

    def test_reorganize_string__abb(self):
        self.assertEqual("bab", ReorganizeString().reorganizeString("abb"))

    def test_reorganize_string__abbc(self):
        self.assertEqual("bcbab", ReorganizeString().reorganizeString("abbbc"))
