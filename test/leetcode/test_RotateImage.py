from unittest import TestCase

from pyquiz.leetcode.RotateImage import RotateImage


class TestRotateImage(TestCase):

    def test_rotate__example1(self):
        """
        Example 1:
        Input: matrix = [[1,2,3],
                        [4,5,6],
                        [7,8,9]]
        Output: [[7,4,1],
                [8,5,2],
                [9,6,3]]
        """
        matrix = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]
        expected = [[7, 4, 1],
                    [8, 5, 2],
                    [9, 6, 3]]
        RotateImage().rotate(matrix)
        self.assertEquals(expected, matrix)

    def test_rotate__example2(self):
        """
        Example 2:
        Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        """
        matrix = [[5, 1, 9, 11],
                  [2, 4, 8, 10],
                  [13, 3, 6, 7],
                  [15, 14, 12, 16]]
        expected = [[15, 13, 2, 5],
                    [14, 3, 4, 1],
                    [12, 6, 8, 9],
                    [16, 7, 10, 11]]
        RotateImage().rotate(matrix)
        self.assertEquals(expected, matrix)

    def test_rotate__example3(self):
        """
        Example 3:
        Input: matrix = [[1]]
        Output: [[1]]
        """
        matrix = [[1]]
        expected = [[1]]
        out = RotateImage().rotate(matrix)
        self.assertEquals(expected, matrix)

    def test_rotate__example4(self):
        """
        Example 4:
        Input: matrix = [[1,2],[3,4]]
        Output: [[3,1],[4,2]]
        """
        matrix = [[1, 2],
                  [3, 4]]
        expected = [[3, 1],
                    [4, 2]]
        RotateImage().rotate(matrix)
        self.assertEquals(expected, matrix)

    def test_rotate__empty(self):
        matrix = []
        expected = []
        RotateImage().rotate(matrix)
        self.assertEquals(expected, matrix)
