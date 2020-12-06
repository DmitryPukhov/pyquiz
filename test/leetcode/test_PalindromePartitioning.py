from unittest import TestCase

from pyquiz.leetcode.PalindromePartitioning import PalindromePartitioning


class TestPalindromePartitioning(TestCase):
    def test_partition__example(self):
        """
        Example:
        Input: "aab"
        Output:
        [
          ["aa","b"],
          ["a","a","b"]
        ]
        """
        actual = PalindromePartitioning().partition("aab")
        self.assertEqual(sorted([["aa", "b"], ["a", "a", "b"]]), sorted(actual))

    def test_partition__empty(self):
        actual = PalindromePartitioning().partition("")
        self.assertEqual([[]], actual)

    def test_partition__a(self):
        actual = PalindromePartitioning().partition("a")
        self.assertEqual([["a"]], actual)

    def test_partition__large(self):
        actual = PalindromePartitioning().partition("abacedasdpeknaaaaaaasdfaso;iqiwe;nokj ncdfasoiqewio;nfo;qiwebo;nifqew")
        self.assertIsNotNone(actual)
