from unittest import TestCase

from pyquiz.leetcode.RobotBoundedInCircle import RobotBoundedInCircle


class TestRobotBoundedInCircle(TestCase):

    def test_is_robot_bounded__ggllgg(self):
        """
        Example 1:
        Input: "GGLLGG"
        Output: true
        """
        self.assertTrue(RobotBoundedInCircle().isRobotBounded("GGLLGG"))

    def test_is_robot_bounded__gg(self):
        """
        Example 2:
        Input: "GG"
        Output: false
        Explanation:
        The robot moves north indefinitely.
        """
        self.assertFalse(RobotBoundedInCircle().isRobotBounded("GG"))

    def test_is_robot_bounded__gl(self):
        """
        Example 3:
        Input: "GL"
        Output: true
        Explanation:
        """
        self.assertTrue(RobotBoundedInCircle().isRobotBounded("GL"))

    def test_is_robot_bounded__gr(self):
        self.assertTrue(RobotBoundedInCircle().isRobotBounded("GR"))

    def test_is_robot_bounded__rl(self):
        self.assertTrue(RobotBoundedInCircle().isRobotBounded("RL"))

    def test_is_robot_bounded__grl(self):
        self.assertFalse(RobotBoundedInCircle().isRobotBounded("GRL"))

    def test_is_robot_bounded__grlgrrgg(self):
        self.assertTrue(RobotBoundedInCircle().isRobotBounded("GRLGRRGG"))

    def test_is_robot_bounded__glrgllgg(self):
        self.assertTrue(RobotBoundedInCircle().isRobotBounded("GLRGLLGG"))
