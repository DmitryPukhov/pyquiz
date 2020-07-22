from unittest import TestCase

from pyquiz.leetcode.RectangleOverlap import RectangleOverlap


class TestRectangleOverlap(TestCase):
    def test_is_rectangle_overlap__overlap(self):
        self.assertTrue(RectangleOverlap().isRectangleOverlap([0, 0, 2, 2], [1, 1, 3, 3]))
        self.assertTrue(RectangleOverlap().isRectangleOverlap([1, 1, 3, 3], [0, 0, 2, 2]))
        self.assertTrue(RectangleOverlap().isRectangleOverlap([0, 0, 2, 2], [-1, -1, 1, 1]))
        self.assertTrue(RectangleOverlap().isRectangleOverlap([7, 8, 13, 15], [10, 8, 12, 20]))

    def test_is_rectangle_overlap__contains(self):
        # One rect is inside another
        self.assertTrue(RectangleOverlap().isRectangleOverlap([1, 1, 1.5, 1.5], [0, 0, 2, 2]))
        self.assertTrue(RectangleOverlap().isRectangleOverlap([0, 0, 2, 2], [1, 1, 1.5, 1.5]))

    def test_is_rectangle_overlap__dontoverlap(self):
        self.assertFalse(RectangleOverlap().isRectangleOverlap([0, 0, 2, 2], [3, 3, 4, 4]))
        self.assertFalse(RectangleOverlap().isRectangleOverlap([0, 0, 2, 2], [-4, -4, -3, -3]))
        self.assertFalse(RectangleOverlap().isRectangleOverlap([0,0,1,1],[1,0,2,1]))

        # ???
        # Details
        # Input
        # [5,15,8,18]
        # [0,3,7,9]
        # Output
        # true
        # Expected
        # false
        self.assertFalse(RectangleOverlap().isRectangleOverlap([5, 15, 8, 18], [0, 3, 7, 9]))

    def test_is_rectangle_overlap__negarea(self):
        # One rect has negative area (bottom left is above upper right)
        self.assertFalse(RectangleOverlap().isRectangleOverlap([0, 0, 2, 2], [1, 1, 0.9, 0.9]))
        self.assertFalse(RectangleOverlap().isRectangleOverlap([1, 1, 0.9, 0.9], [0, 0, 2, 2]))

    def test_is_rectangle_overlap__one_inside_other(self):
        # One rect is inside other and 2 has the same width or height
        self.assertTrue(RectangleOverlap().isRectangleOverlap([0, 0, 3, 3], [0, 1, 1, 2]))

