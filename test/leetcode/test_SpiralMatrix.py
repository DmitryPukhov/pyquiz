from unittest import TestCase

from pyquiz.leetcode.SpiralMatrix import SpiralMatrix


class TestSpiralMarix(TestCase):
    def test_spiral_order__example1(self):
        """
        Example 1:
        Input:
        [
            [ 1, 2, 3 ],
            [ 4, 5, 6 ],
            [ 7, 8, 9 ]
        ]
        Output: [1,2,3,6,9,8,7,4,5]
        """
        input_ = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        output = [1, 2, 3, 6, 9, 8, 7, 4, 5]
        self.assertEqual(output, SpiralMatrix().spiralOrder(input_))

    def test_spiral_order__example2(self):
        """
        Example 2:
        Input:
        [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9,10,11,12]
        ]
        Output: [1,2,3,4,8,12,11,10,9,5,6,7]
        """
        input_ = [
            [1, 2,  3,  4],
            [5, 6,  7,  8],
            [9, 10, 11, 12]
        ]
        output = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
        self.assertEqual(output, SpiralMatrix().spiralOrder(input_))

    def test_spiral_order__1(self):
        self.assertEqual([1], SpiralMatrix().spiralOrder([[1]]))

    def test_spiral_order__1_2(self):
        self.assertEqual([1, 2], SpiralMatrix().spiralOrder([[1, 2]]))

    def test_spiral_order__1__2(self):
        self.assertEqual([1, 2], SpiralMatrix().spiralOrder([[1], [2]]))

    def test_spiral_order__1__2__3__4(self):
        self.assertEqual([1, 2, 3, 4], SpiralMatrix().spiralOrder([[1], [2], [3], [4]]))

    def test_spiral_order__1_2__3_4(self):
        self.assertEqual([1, 2, 4, 3], SpiralMatrix().spiralOrder([[1, 2], [3, 4]]))

    def test_spiral_order__1234(self):
        self.assertEqual([1, 2, 3, 4], SpiralMatrix().spiralOrder([[1, 2, 3, 4]]))

    def test_spiral_order__empty2d(self):
        self.assertEqual([], SpiralMatrix().spiralOrder([[]]))

    def test_spiral_order__empty1d(self):
        self.assertEqual([], SpiralMatrix().spiralOrder([]))

    def test_spiral_order__none(self):
        self.assertEqual([], SpiralMatrix().spiralOrder(None))
