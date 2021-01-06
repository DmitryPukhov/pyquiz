from unittest import TestCase

from pyquiz.leetcode.AlienDictionary import AlienDictionary


class TestAlienDictionary(TestCase):

    def test_alien_order__example1(self):
        """
        Example 1:
        Input: words = ["wrt","wrf","er","ett","rftt"]
        Output: "wertf"
        """
        out = AlienDictionary().alienOrder(["wrt", "wrf", "er", "ett", "rftt"])
        self.assertEqual("wertf", out)

    def test_alien_order__example2(self):
        """
        Example 2:
        Input: words = ["z","x"]
        Output: "zx"
        """
        out = AlienDictionary().alienOrder(["z", "x"])
        self.assertEqual("zx", out)

    def test_alien_order__example3(self):
        """
        Example 3:
        Input: words = ["z","x","z"]
        Output: ""
        Explanation: The order is invalid, so return "".
        """
        out = AlienDictionary().alienOrder(["z", "x", "z"])
        self.assertEqual("", out)

    def test_alien_order__cycle(self):
        out = AlienDictionary().alienOrder(["ab", "ba", "ab"])
        self.assertEqual("", out)

    def test_aleen_order_case2(self):
        out = AlienDictionary().alienOrder(["ac","ab","zc","zb"])
        self.assertEqual("aczb", out)