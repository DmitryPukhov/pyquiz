from unittest import TestCase
from pyquiz.leetcode.StringCompression2 import Solution


class TestSolution(TestCase):

    def test_get_length_of_optimal_compression_example1(self):
        """
        Example 1:
        Input: s = "aaabcccd", k = 2
        Output: 4
        Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6.
        Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5,
        for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d.
        Therefore, the optimal way is to delete 'b' and 'd',
        then the compressed version of s will be "a3c3" of length 4.
        """
        out = Solution().getLengthOfOptimalCompression(s="aaabcccd", k=2)
        self.assertEqual(4, out)

    def test_get_length_of_optimal_compression_example2(self):
        """
        Example 2:
        Input: s = "aabbaa", k = 2
        Output: 2
        Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.
        """
        out = Solution().getLengthOfOptimalCompression(s="aabbaa", k=2)
        self.assertEqual(2, out)

    def test_get_length_of_optimal_compression_example3(self):
        """
        Example 3:
        Input: s = "aaaaaaaaaaa", k = 0
        Output: 3
        Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.
        """
        out = Solution().getLengthOfOptimalCompression(s="aaaaaaaaaaa", k=0)
        self.assertEqual(3, out)
