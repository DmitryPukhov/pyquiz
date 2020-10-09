from unittest import TestCase

from pyquiz.leetcode.GenerateParentheses import GenerateParentheses


class TestGenerateParentheses(TestCase):

    def test_generate_parenthesis_3(self):
        self.assertEqual(["((()))", "(()())", "(())()", "()(())", "()()()"],
                         GenerateParentheses().generateParenthesis(3))

    def test_generate_parenthesis_1(self):
        self.assertEqual(["()"], GenerateParentheses().generateParenthesis(1))
