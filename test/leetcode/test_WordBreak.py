from unittest import TestCase

from pyquiz.leetcode.WordBreak import WordBreak


class TestWordBreak(TestCase):
    def test_word_break__leetcode(self):
        """
        Example 1:
        Input: s = "leetcode", wordDict = ["leet", "code"]
        Output: true
        Explanation: Return true because "leetcode" can be segmented as "leet code".
        """
        self.assertTrue(WordBreak().wordBreak("leetcode", ["leet", "code"]))

    def test_word_break__applepenapple(self):
        """
        Example 2:
        Input: s = "applepenapple", wordDict = ["apple", "pen"]
        Output: true
        Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
        """
        self.assertTrue(WordBreak().wordBreak("applepenapple", ["apple", "pen"]))

    def test_word_break__catsandog(self):
        """
        Example 3:
        Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
        Output: false
        """
        self.assertFalse(WordBreak().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))

    def test_word_break__godnessgod(self):
        self.assertTrue(WordBreak().wordBreak("godnessgod", ["godness", "god"]))

    def test_word_break__godnessgod(self):
        self.assertTrue(WordBreak().wordBreak("godnessgod", ["godness", "god"]))

    def test_word_break__empty_str(self):
        self.assertFalse(WordBreak().wordBreak("", ["a", "b"]))

    def test_word_break__none_str(self):
        self.assertFalse(WordBreak().wordBreak(None, ["a", "b"]))

    def test_word_break__none_dict(self):
        self.assertFalse(WordBreak().wordBreak("a", None))

    def test_word_break__none_str_dict(self):
        self.assertFalse(WordBreak().wordBreak(None, None))

    def test_word_break__none_str_dict(self):
        self.assertFalse(WordBreak().wordBreak(None, None))

    def test_word_break__abc(self):
        self.assertTrue(WordBreak().wordBreak("abc", ["a", "b", "bc"]))

    def test_word_break__longa(self):
        self.assertTrue(WordBreak().wordBreak(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
            ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]))

    def test_word_break__a(self):
        self.assertTrue(WordBreak().wordBreak(
            "a",
            ["a"]))
