from unittest import TestCase

from pyquiz.leetcode.DecodeXoredArray import Solution


class TestSolution(TestCase):

    def test_decode_example1(self):
        """
        Example 1:
        Input: encoded = [1,2,3], first = 1
        Output: [1,0,2,1]
        Explanation: If arr = [1,0,2,1], then first = 1 and encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
        """
        out = Solution().decode(encoded=[1, 2, 3], first=1)
        self.assertEqual([1, 0, 2, 1], out)

    def test_decode_example2(self):
        """
        Example 2:
        Input: encoded = [6,2,7,3], first = 4
        Output: [4,2,0,7,4]
        """
        out = Solution().decode(encoded=[6, 2, 7, 3], first=4)
        self.assertEqual([4, 2, 0, 7, 4], out)
