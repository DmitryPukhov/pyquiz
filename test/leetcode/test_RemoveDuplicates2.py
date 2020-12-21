from unittest import TestCase

from pyquiz.leetcode.RemoveDuplicates2 import RemoveDuplicates2


class TestRemoveDuplicates2(TestCase):
    def test_remove_duplicates__example1(self):
        """
        Example 1:
        Input: s = "abcd", k = 2
        Output: "abcd"
        Explanation: There's nothing to delete.
        """
        res = RemoveDuplicates2().removeDuplicates("abcd",2)
        self.assertEqual("abcd",res)

    def test_remove_duplicates__example2(self):
        """
        Example 2:
        Input: s = "deeedbbcccbdaa", k = 3
        Output: "aa"
        Explanation:
        First delete "eee" and "ccc", get "ddbbbdaa"
        Then delete "bbb", get "dddaa"
        Finally delete "ddd", get "aa"
        """
        res = RemoveDuplicates2().removeDuplicates("deeedbbcccbdaa",3)
        self.assertEqual("aa",res)

    def test_remove_duplicates__example3(self):
        """
        Example 3:
        Input: s = "pbbcggttciiippooaais", k = 2
        Output: "ps"
        """
        res = RemoveDuplicates2().removeDuplicates("pbbcggttciiippooaais",2)
        self.assertEqual("ps",res)

    def test_remove_duplicates__example3(self):
        """
        Example 3:
        Input: s = "pbbcggttciiippooaais", k = 2
        Output: "ps"
        """
        res = RemoveDuplicates2().removeDuplicates("pbbcggttciiippooaais",2)
        self.assertEqual("ps",res)

    def test_remove_duplicates_a_2(self):
        res = RemoveDuplicates2().removeDuplicates("a",2)
        self.assertEqual("a",res)

    def test_remove_duplicates_aa_2(self):
        res = RemoveDuplicates2().removeDuplicates("aa",2)
        self.assertEqual("",res)

    def test_remove_duplicates_baa_2(self):
        res = RemoveDuplicates2().removeDuplicates("baa",2)
        self.assertEqual("b",res)

    def test_remove_duplicates_aab_2(self):
        res = RemoveDuplicates2().removeDuplicates("aab",2)
        self.assertEqual("b",res)

    def test_remove_duplicates_aaab_2(self):
        res = RemoveDuplicates2().removeDuplicates("aaab",2)
        self.assertEqual("ab",res)

    def test_remove_duplicates_aaabba_2(self):
        res = RemoveDuplicates2().removeDuplicates("aaabba",2)
        self.assertEqual("",res)
