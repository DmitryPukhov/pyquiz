from unittest import TestCase

from pyquiz.leetcode.BasicCalculator import BasicCalculator


class TestBasicCalculator(TestCase):
    def test_calculate_example1(self):
        """
        Example 1:
        Input: "1 + 1"
        Output: 2
        """
        out = BasicCalculator().calculate("1 + 1")
        self.assertEqual(2, out)

    def test_calculate_example2(self):
        """
        Example 2:
        Input: " 2-1 + 2 "
        Output: 3
        """
        out = BasicCalculator().calculate(" 2-1 + 2 ")
        self.assertEqual(3, out)

    def test_calculate_example3(self):
        """
        Example 3:
        Input: "(1+(4+5+2)-3)+(6+8)"
        Output: 23
        """
        out = BasicCalculator().calculate("(1+(4+5+2)-3)+(6+8)")
        self.assertEqual(23, out)

    def test_calculate_example3(self):
        """
        Example 3:
        Input: "(1+(4+5+2)-3)+(6+8)"
        Output: 23
        """
        out = BasicCalculator().calculate("(1+(4+5+2)-3)+(6+8)")
        self.assertEqual(23, out)

    def test_calculate_example_1(self):
        out = BasicCalculator().calculate("1")
        self.assertEqual(1, out)

    def test_calculate_example_1inbrackets(self):
        out = BasicCalculator().calculate("(1)")
        self.assertEqual(1, out)

    def test_calculate_example_1inmultibrackets(self):
        out = BasicCalculator().calculate("((1))")
        self.assertEqual(1, out)

    def test_calculate_example_1plus1(self):
        out = BasicCalculator().calculate("(1+1)")
        self.assertEqual(2, out)

    def test_calculate_example_manybrackets(self):
        #out = BasicCalculator().calculate("((1+2-1+4)+1)+1-(3-(5-7-(1)))")
        out = BasicCalculator().calculate("((1+2-1+4)+1)+1-(3-(5-7-(1)))")
        self.assertEqual(2, out)

    def test_calculate_example_123(self):
        out = BasicCalculator().calculate("1+2+3")
        self.assertEqual(6, out)

    def test_calculate_example_3mb1m2(self):
        out = BasicCalculator().calculate("3-(1-2)")
        self.assertEqual(4, out)

    def test_neg2plus1(self):
        out = BasicCalculator().calculate("-2+1")
        self.assertEqual(-1,out)

    def test_1plusneg2(self):
        out = BasicCalculator().calculate("1+-2")
        self.assertEqual(-1,out)

    def test_1minusneg2(self):
        # ??? But 1- -2 expects
        out = BasicCalculator().calculate("1--2")
        self.assertEqual(-1,out)

    def test_minusbefore(self):
        # ??? But 1- -2 expects
        # - (3 + (4 + 5))
        out = BasicCalculator().calculate("-(3-1)")
        self.assertEqual(-2,out)
