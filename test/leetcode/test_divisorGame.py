from unittest import TestCase

from pyzuiz.leetcode.DivisorGame import DivisorGame


class TestDivisorGame(TestCase):
    def test_divisorGame(self):
        algo = DivisorGame()
        for n in range(1, 1000):
            print(n)
            self.assertEqual(n % 2 == 0, algo.divisorGame(n), f"n={n}")
