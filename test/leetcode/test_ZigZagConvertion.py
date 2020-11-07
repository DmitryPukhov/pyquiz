from unittest import TestCase

from pyquiz.leetcode.ZigZagConvertion import ZigZagConversion


class TestZigZagConversion(TestCase):

    def test_convert_example1(self):
        """
        Example 1:
        Input: s = "PAYPALISHIRING", numRows = 3
        Output: "PAHNAPLSIIGYIR"
        """
        out = ZigZagConversion().convert("PAYPALISHIRING", 3)
        self.assertEqual("PAHNAPLSIIGYIR", out)

    def test_convert_example2(self):
        """
        Example 2:
        Input: s = "PAYPALISHIRING", numRows = 4
        Output: "PINALSIGYAHRPI"
        Explanation:
        P     I    N
        A   L S  I G
        Y A   H R
        P     I
        """
        out = ZigZagConversion().convert("PAYPALISHIRING", 4)
        self.assertEqual("PINALSIGYAHRPI", out)

    def test_convert_example3(self):
        """
        Example 3:
        Input: s = "A", numRows = 1
        Output: "A"
        """
        out = ZigZagConversion().convert("A", 1)
        self.assertEqual("A", out)

    def test_convert__abc_d_efg3(self):
        """
        a   e
        b d f
        c   g
        """
        out = ZigZagConversion().convert("abcdefg", 3)
        self.assertEqual("aebdfcg", out)

    def test_convert__abc_d_3(self):
        """
        a
        b d
        c
        """
        out = ZigZagConversion().convert("abcd", 3)
        self.assertEqual("abdc", out)

    def test_convert__ab_cd_2(self):
        """
        a c
        b d

        """
        out = ZigZagConversion().convert("abcd", 2)
        self.assertEqual("acbd", out)