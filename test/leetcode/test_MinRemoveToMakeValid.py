from unittest import TestCase

from pyquiz.leetcode.MinRemoveToMakeValid import MinRemoveToMakeValid


class TestMinRemoveToMakeValid(TestCase):

    def test_min_remove_to_make_valid__lee1t1c2o2de2(self):
        """
        Example 1:
        Input: s = "lee(t(c)o)de)"
        Output: "lee(t(c)o)de"
        Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
        """
        self.assertEqual("lee(t(c)o)de", MinRemoveToMakeValid().minRemoveToMakeValid("lee(t(c)o)de)"))

    def test_min_remove_to_make_valid__a2b1c2d(self):
        """
        Example 2:
        Input: s = "a)b(c)d"
        Output: "ab(c)d"
        """
        self.assertEqual("ab(c)d", MinRemoveToMakeValid().minRemoveToMakeValid("a)b(c)d"))

    def test_min_remove_to_make_valid__2211(self):
        """
        Example 3:
        Input: s = "))((""
        Output: ""
        """
        self.assertEqual("", MinRemoveToMakeValid().minRemoveToMakeValid("))(("))

    def test_min_remove_to_make_valid__1a1b1c2d2(self):
        """
        Example 4:
        Input: s = "(a(b(c)d)"
        Output: "a(b(c)d)"
        """
        self.assertEqual("a(b(c)d)", MinRemoveToMakeValid().minRemoveToMakeValid("a(b(c)d)"))

    def test_min_remove_to_make_valid__singleletter(self):
        self.assertEqual("a", MinRemoveToMakeValid().minRemoveToMakeValid("a"))

    def test_min_remove_to_make_valid__1(self):
        self.assertEqual("", MinRemoveToMakeValid().minRemoveToMakeValid("("))

    def test_min_remove_to_make_valid__2(self):
        self.assertEqual("", MinRemoveToMakeValid().minRemoveToMakeValid(")"))

    def test_min_remove_to_make_valid__112(self):
        self.assertEqual("()", MinRemoveToMakeValid().minRemoveToMakeValid("(()"))

    def test_min_remove_to_make_valid__122(self):
        self.assertEqual("()", MinRemoveToMakeValid().minRemoveToMakeValid("())"))
