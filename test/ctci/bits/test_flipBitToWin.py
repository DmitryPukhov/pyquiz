from unittest import TestCase

from pyquiz.ctci.bits.FlipBitToWin import FlipBitToWin


class TestFlipBitToWin(TestCase):
    def test_longest_seq_normal_case(self):
        cnt = FlipBitToWin().longest_seq(0b1101110)
        self.assertEqual(6, cnt)

    def test_longest_seq_with_all_0_should_be_one(self):
        # Zero bits but we can flip 1, so the result is 1
        cnt = FlipBitToWin().longest_seq(0b00000)
        self.assertEqual(1, cnt)

    def test_longest_seq_with_all_1_should_be_33(self):
        # Zero bits but we can flip 1, so the result is 1
        cnt = FlipBitToWin().longest_seq(0xFFFFFFFF)
        self.assertEqual(33, cnt)

    def test_longest_seq(self):
        cnt = FlipBitToWin().longest_seq(0b101010)
        self.assertEqual(3, cnt)
