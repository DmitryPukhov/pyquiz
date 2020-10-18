from unittest import TestCase

from pyquiz.leetcode.LetterCombinations import LetterCombinations


class TestLetterCombinations(TestCase):

    def test_letter_combinations__example1(self):
        """
        Example 1:
        Input: digits = "23"
        Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        """
        res = LetterCombinations().letterCombinations("23")
        self.assertEqual(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"], res)

    def test_letter_combinations__example2(self):
        """
        Example 2:
        Input: digits = ""
        Output: []
        """
        res = LetterCombinations().letterCombinations("")
        self.assertEqual([], res)

    def test_letter_combinations__example3(self):
        """
        Example 3:
        Input: digits = "2"
        Output: ["a","b","c"]
        """
        res = LetterCombinations().letterCombinations("2")
        self.assertEqual(["a", "b", "c"], res)
