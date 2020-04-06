from unittest import TestCase

from pyzuiz.leetcode.AddBinary import AddBinary


class TestAddBinary(TestCase):
    """
    Given two binary strings, return their sum (also a binary string).
    The input strings are both non-empty and contains only characters 1 or 0.
    Example 1:
    Input: a = "11", b = "1"
    Output: "100"
    Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"
    """

    def test_add_binary(self):
        alg = AddBinary()
        #self.assertEqual('100', alg.addBinary('11', '1'))
        self.assertEqual('10101', alg.addBinary('1010', '1011'))

