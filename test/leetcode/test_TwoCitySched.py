from unittest import TestCase

from pyquiz.leetcode.TwoCitySched import TwoCitySched


class TestTwoCitySched(TestCase):
    def test_two_city_sched_cost(self):
        self.assertEqual(110, TwoCitySched().twoCitySchedCost(([[10, 20], [30, 200], [400, 50], [30, 20]])))
        self.assertEqual(60, TwoCitySched().twoCitySchedCost(([[10, 20], [10, 20], [10, 20], [10, 20]])))
        self.assertEqual(40, TwoCitySched().twoCitySchedCost(([[1000, 10], [10, 1000], [1000, 10], [10, 1000]])))
        self.assertEqual(430, TwoCitySched().twoCitySchedCost(([[10, 20], [10, 1000], [100, 200], [200, 300]])))
