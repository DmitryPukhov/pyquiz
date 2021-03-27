from unittest import TestCase
from pyquiz.leetcode.EditDistance import Solution


class TestSolution(TestCase):
    def test_min_distance__example1(self):
        """
        Example 1:
        Input: word1 = "horse", word2 = "ros"
        Output: 3
        Explanation:
        horse -> rorse (replace 'h' with 'r')
        rorse -> rose (remove 'r')
        rose -> ros (remove 'e')
        """
        self.assertEqual(3, Solution().minDistance(word1="horse", word2="ros"))

    def test_min_distance__example2(self):
        """
        Example 2:
        Input: word1 = "intention", word2 = "execution"
        Output: 5
        Explanation:
        intention -> inention (remove 't')
        inention -> enention (replace 'i' with 'e')
        enention -> exention (replace 'n' with 'x')
        exention -> exection (replace 'n' with 'c')
        exection -> execution (insert 'u')
        """
        self.assertEqual(5, Solution().minDistance(word1="intention", word2="execution"))

    def test_is_one_edit_distance__example1(self):
        """
        Example 1:
        Input: s = "ab", t = "acb"
        Output: true
        Explanation: We can insert 'c' into s to get t.
        """
        self.assertEquals(1, Solution().minDistance(word1="ab", word2="acb"))

    def test_is_one_edit_distance__example2(self):
        """
        Example 2:
        Input: s = "", t = ""
        Output: false
        Explanation: We cannot get t from s by only one step.
        """
        self.assertEquals(0, Solution().minDistance(word1="", word2=""))

    def test_is_one_edit_distance__example3(self):
        """
        Example 3:
        Input: s = "a", t = ""
        Output: true
        """
        self.assertEquals(1, Solution().minDistance(word1="a", word2=""))

    def test_is_one_edit_distance__example4(self):
        """
        Example 4:
        Input: s = "", t = "A"
        Output: true
        """
        self.assertEquals(1, Solution().minDistance(word1="", word2="A"))

    def test_is_one_edit_distance__a_a(self):
        self.assertEquals(0, Solution().minDistance(word1="a", word2="a"))

    def test_is_one_edit_distance__large(self):
        self.assertIsNotNone(Solution().minDistance(word1="asdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewa", word2="aasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewaasdfawecvaswewrfeawfaweawcffaewa"))
