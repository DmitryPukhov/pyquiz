from unittest import TestCase

from pyquiz.leetcode.DecodeWays import DecodeWays


class TestDecodeWays(TestCase):
    def test_num_decodings__1(self):
        self.assertEqual(1, DecodeWays().numDecodings("1"))

    def test_num_decodings__0(self):
        self.assertEqual(0, DecodeWays().numDecodings("0"))

    def test_num_decodings__00(self):
        self.assertEqual(0, DecodeWays().numDecodings("00"))

    def test_num_decodings__000(self):
        self.assertEqual(0, DecodeWays().numDecodings("000"))

    def test_num_decodings__11(self):
        self.assertEqual(2, DecodeWays().numDecodings("11"))

    def test_num_decodings__01(self):
        self.assertEqual(0, DecodeWays().numDecodings("01"))

    def test_num_decodings__10(self):
        self.assertEqual(1, DecodeWays().numDecodings("10"))

    def test_num_decodings__12(self):
        self.assertEqual(2, DecodeWays().numDecodings("12"))

    def test_num_decodings__011(self):
        self.assertEqual(0, DecodeWays().numDecodings("011"))

    def test_num_decodings__101(self):
        self.assertEqual(1, DecodeWays().numDecodings("101"))

    def test_num_decodings__110(self):
        self.assertEqual(1, DecodeWays().numDecodings("110"))

    def test_num_decodings__111(self):
        self.assertEqual(3, DecodeWays().numDecodings("111"))

    def test_num_decodings__711(self):
        self.assertEqual(2, DecodeWays().numDecodings("711"))

    def test_num_decodings__171(self):
        self.assertEqual(2, DecodeWays().numDecodings("171"))

    def test_num_decodings__117(self):
        self.assertEqual(3, DecodeWays().numDecodings("117"))
