from unittest import TestCase
from pyquiz.leetcode.RansomNote import Solution


class TestSolution(TestCase):

    def test_can_construct__example1(self):
        """
        Example 1:
        Input: ransomNote = "a", magazine = "b"
        Output: false
        """
        self.assertFalse(Solution().canConstruct("a", "b"))

    def test_can_construct__example2(self):
        """
        Example 2:
        Input: ransomNote = "aa", magazine = "ab"
        Output: false
        """
        self.assertFalse(Solution().canConstruct(ransomNote="aa", magazine="ab"))

    def test_can_construct__example3(self):
        """
        Example 3:
        Input: ransomNote = "aa", magazine = "aab"
        Output: true
        """
        self.assertTrue(Solution().canConstruct( ransomNote = "aa", magazine = "aab"))
