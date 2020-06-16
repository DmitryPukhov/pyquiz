from unittest import TestCase

from pyquiz.leetcode.DestinationCity import DestinationCity


class TestDestinationCity(TestCase):

    def test_dest_city(self):
        dest = DestinationCity().dest_city([["A", "Z"]])
        self.assertEqual("Z", dest)
        dest = DestinationCity().dest_city_singleline([["A", "Z"]])
        self.assertEqual("Z", dest)

        dest = DestinationCity().dest_city([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
        self.assertEqual("Sao Paulo", dest)
        dest = DestinationCity().dest_city_singleline([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
        self.assertEqual("Sao Paulo", dest)
