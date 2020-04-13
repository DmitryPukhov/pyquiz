from unittest import TestCase

from pyquiz.leetcode.ValidParentheses import ValidParentheses


class TestValidParentheses(TestCase):
    alg = ValidParentheses()

    def test_isValid__valid(self):
        self.assertTrue(self.alg.isValid("[](){}"))
        self.assertTrue(self.alg.isValid("([{}])"))

    def test_isValid__not_valid(self):
        self.assertFalse(self.alg.isValid("("))
        self.assertFalse(self.alg.isValid("[)"))
        self.assertFalse(self.alg.isValid(")("))
        self.assertFalse(self.alg.isValid(")"))
        self.assertFalse(self.alg.isValid("([{}]))"))

    def test_isValid__odd_items__not_valid(self):
        self.assertFalse(self.alg.isValid(")"))

    def test_isValid__empty(self):
        self.assertTrue(self.alg.isValid(""))
