from unittest import TestCase

from pyquiz.leetcode.DecodeString import DecodeString


class TestDecodeString(TestCase):
    """
    Example 2:
    Input: s = "3[a2[c]]"
    Output: "accaccacc"

    Example 3:
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"

    Example 4:
    Input: s = "abc3[cd]xyz"
    Output: "abccdcdcdxyz"
    """

    def test_decode_string__3a2bc(self):
        """
        Example 1:
        Input: s = "3[a]2[bc]"
        Output: "aaabcbc"
        """
        self.assertEqual("aaabcbc", DecodeString().decodeString("3[a]2[bc]"))

    def test_decode_string__3a2c(self):
        """
        Example 2:
        Input: s = "3[a2[c]]"
        Output: "accaccacc"
        """
        self.assertEqual("accaccacc", DecodeString().decodeString("3[a2[c]]"))

    def test_decode_string__2abc3cdef(self):
        """
        Example 3:
        Input: s = "2[abc]3[cd]ef"
        Output: "abcabccdcdcdef"
        """
        self.assertEqual("abcabccdcdcdef", DecodeString().decodeString("2[abc]3[cd]ef"))

    def test_decode_string__3a2bc(self):
        """
        Example 4:
        Input: s = "abc3[cd]xyz"
        Output: "abccdcdcdxyz"
        """
        self.assertEqual("abccdcdcdxyz", DecodeString().decodeString("abc3[cd]xyz"))

    def test_decode_string__empty(self):
        self.assertEqual("", DecodeString().decodeString(""))

    def test_decode_string__a(self):
        self.assertEqual("a", DecodeString().decodeString("a"))
