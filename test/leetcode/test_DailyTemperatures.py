from random import Random
from unittest import TestCase
from pyquiz.leetcode.DailyTemperatures import Solution


class TestSolution(TestCase):

    def test_daily_temperatures__example1(self):
        """
        For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
        your output should be [1, 1, 4, 2, 1, 1, 0, 0].
        """
        self.assertEqual([1, 1, 4, 2, 1, 1, 0, 0], Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))

    def test_daily_temperatures__12(self):
        self.assertEqual([1, 0], Solution().dailyTemperatures([1, 2]))

    def test_daily_temperatures__11(self):
        self.assertEqual([0, 0], Solution().dailyTemperatures([1, 1]))

    def test_daily_temperatures__121(self):
        self.assertEqual([1, 0, 0], Solution().dailyTemperatures([1, 2, 1]))

    def test_daily_temperatures__1231(self):
        self.assertEqual([1, 1, 0, 0], Solution().dailyTemperatures([1, 2, 3, 1]))

    def test_daily_temperatures__11153110(self):
        self.assertEqual([1, 1, 5, 3, 1, 1, 1, 0], Solution().dailyTemperatures([1, 2, 3, 2, 1, 2, 3, 4]))

    def test_daily_temperatures__1(self):
        self.assertEqual([0], Solution().dailyTemperatures([1]))

    def test_daily_temperatures__empty(self):
        self.assertEqual([], Solution().dailyTemperatures([]))

    def test_daily_temperatures__large(self):
        r = Random()
        self.assertIsNotNone(Solution().dailyTemperatures([r.randint(30,100) for i in range(0,1000000)]))
