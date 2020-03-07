from unittest import TestCase

from pyzuiz.leetcode.ReverseInteger import ReverseInteger


class TestReverseInteger(TestCase):
    algo = ReverseInteger()

    def test_reverse(self):
        print(f'-2^31={-2**31}, 2^31-1 = {2**31 - 1}')
        self.assertEqual(0, self.algo.reverse(1534236469))
        self.assertEqual(321, self.algo.reverse(123))
        self.assertEqual(-321, self.algo.reverse(-123))

    def test_digit(self):
        self.assertEqual(3, self.algo.digit(123, 0))
        self.assertEqual(2, self.algo.digit(123, 1))
        self.assertEqual(1, self.algo.digit(123, 2))
