from unittest import TestCase

from pyzuiz.leetcode.MinCostClimbingStairs import MinCostClimbingStairs


class TestMinCostClimbingStairs(TestCase):
    def test_min_cost_climbing_stairs(self):
        alg = MinCostClimbingStairs()

        cost = alg.minCostClimbingStairs([10, 15, 20])
        self.assertEqual(15, cost)

        cost = alg.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])
        self.assertEqual(6, cost)

        cost = alg.minCostClimbingStairs([1, 1, 1])
        self.assertEqual(1, cost)
