from unittest import TestCase

from pyquiz.leetcode.FriendCircles import FriendCircles


class TestFriendCircles(TestCase):
    def test_find_circle_num__example1(self):
        """
        Example 1:
        Input:
        [[1,1,0],
         [1,1,0],
         [0,0,1]]
        Output: 2
        """
        m = [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]]
        num = FriendCircles().findCircleNum(m)
        self.assertEqual(2, num)

    def test_find_circle_num__example2(self):
        """
        Example 2:
        Input:
        [[1,1,0],
         [1,1,1],
         [0,1,1]]
        Output: 1
        """
        m = [[1, 1, 0],
             [1, 1, 1],
             [0, 1, 1]]

        num = FriendCircles().findCircleNum(m)
        self.assertEqual(1, num)

    def test_find_circle_num__100_010_001(self):
        m = [[1, 0, 0],
             [0, 1, 0],
             [0, 0, 1]]
        num = FriendCircles().findCircleNum(m)
        self.assertEqual(3, num)

    def test_find_circle_num__10_110_001(self):
        m = [[1, 1, 0],
             [1, 1, 0],
             [0, 0, 1]]
        num = FriendCircles().findCircleNum(m)
        self.assertEqual(2, num)

    def test_find_circle_num__100_011_011(self):
        m = [[1, 0, 0],
             [0, 1, 1],
             [0, 1, 1]]
        num = FriendCircles().findCircleNum(m)
        self.assertEqual(2, num)

    def test_find_circle_num__1(self):
        m = [[1]]
        num = FriendCircles().findCircleNum(m)
        self.assertEqual(1, num)

    def test_find_circle_num__1000_0100_0010_0001(self):
        m = [[1, 0, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]
             ]
        num = FriendCircles().findCircleNum(m)
        self.assertEqual(4, num)

    def test_find_circle_num__1100_1100_0010_0001(self):
        m = [[1, 1, 0, 0],
             [1, 1, 0, 0],
             [0, 0, 1, 0],
             [0, 0, 0, 1]
             ]
        num = FriendCircles().findCircleNum(m)
        self.assertEqual(3, num)

    def test_find_circle_num__1011_0100_1011_1001(self):
        m = [[1, 0, 1, 1],
             [0, 1, 0, 0],
             [1, 0, 1, 1],
             [1, 0, 1, 1]
             ]
        num = FriendCircles().findCircleNum(m)
        self.assertEqual(2, num)