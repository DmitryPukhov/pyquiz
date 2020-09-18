from unittest import TestCase

from pyquiz.leetcode.ContainerWithMostWater import ContainerWithMostWater


class TestContainerWithMostWater(TestCase):
    def test_max_area__1_8_6_2_5_4_8_3_7(self):
        self.assertEqual(49, ContainerWithMostWater().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

    def test_max_area__empty(self):
        self.assertEqual(0, ContainerWithMostWater().maxArea([]))

    def test_max_area__none(self):
        self.assertEqual(0, ContainerWithMostWater().maxArea([]))

    def test_max_area__1(self):
        self.assertEqual(0, ContainerWithMostWater().maxArea([1]))

    def test_max_area__1_100_2_1(self):
        self.assertEqual(3, ContainerWithMostWater().maxArea([1, 100, 2, 1]))
