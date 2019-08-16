from unittest import TestCase

from pyzuiz.RobotInAGrid import RobotInAGrid


class TestRobotInAGrid(TestCase):

    def test_find_path__2x2_noright(self):
        robot = RobotInAGrid([(0, 1)], 2, 2)
        path = robot.find_path()
        self.assertEquals([(0, 0), (1, 0), (1, 1)], path)

    def test_find_path__2x2_nodown(self):
        robot = RobotInAGrid([(1, 0)], 2, 2)
        path = robot.find_path()
        self.assertEquals([(0, 0), (0, 1), (1, 1)], path)
