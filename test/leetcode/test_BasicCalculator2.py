from unittest import TestCase
from pyquiz.leetcode.BasicCalculator2 import BasicCalculator2


class TestBasicCalculator2(TestCase):
    def test_2minus3div4minus1(self):
        self.assertEqual(32, BasicCalculator2().calculate("1*2-3/4+5*6"))

    def test_example_1mul2minus3div4plus5mul6minus7mul8plus9div10(self):
        self.assertEqual(-24, BasicCalculator2().calculate("1*2-3/4+5*6-7*8+9/10"))

    def test_example_14div3mul2plus14div4mul3(self):
        self.assertEqual(17, BasicCalculator2().calculate("14/3*2+15/4*3"))

    def test_example_14div3mul2div4(self):
        self.assertEqual(2, BasicCalculator2().calculate("14/3*2/4"))

    def test_example_14div3mul2(self):
        self.assertEqual(8, BasicCalculator2().calculate("14/3*2"))

    def test_example_1plus3plus3(self):
        self.assertEqual(6, BasicCalculator2().calculate("1+2+3"))

    def test_example_1mul2plus3mul4(self):
        self.assertEqual(14, BasicCalculator2().calculate("1*2+3*4"))

    def test_example_1plus2mul3plus4mul5(self):
        self.assertEqual(22, BasicCalculator2().calculate("1+2*3+3*5"))

    def test_example_1plus2mul3plus4mul5plus6(self):
        self.assertEqual(28, BasicCalculator2().calculate("1+2*3+3*5+6"))

    def test_example_2mul3plus4mul5plu26(self):
        self.assertEqual(27, BasicCalculator2().calculate("2*3+3*5+6"))

    def test_example1(self):
        """
        Example 1:
        Input: s = "3+2*2"
        Output: 7
        """
        self.assertEqual(7, BasicCalculator2().calculate("3+2*2"))

    def test_example2(self):
        """
        Example 2:

        Input: s = " 3/2 "
        Output: 1
        """
        self.assertEqual(1, BasicCalculator2().calculate("3/2"))

    def test_example3(self):
        """
        Example 3:
        Input: s = " 3+5 / 2 "
        Output: 5
        """
        self.assertEqual(5, BasicCalculator2().calculate("3+5 / 2"))

    def test_example_1(self):
        self.assertEqual(1, BasicCalculator2().calculate("1"))
