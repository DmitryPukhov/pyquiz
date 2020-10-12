from unittest import TestCase

from pyquiz.leetcode.RandomizedSet import RandomizedSet


class TestRandomizedSet(TestCase):
    def test_get_random(self):
        """
        Input
        ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
        [[],              [1],       [2],      [2],     [],           [1],      [2],       []]
        Output
        [null, true, false, true, 2, true, false, 2]
        """
        rs = RandomizedSet()
        for i in range(2):
            rs.remove(2)
            self.assertTrue(rs.insert(1))
            self.assertFalse(rs.remove(2))
            self.assertTrue(rs.insert(2))
            self.assertIsNotNone(rs.getRandom())
            self.assertTrue(rs.remove(1))
            self.assertFalse(rs.insert(2))
            self.assertEqual(2, rs.getRandom())
