from unittest import TestCase

from pyzuiz.leetcode.DayOfTheWeek import DayOfTheWeek


class TestDayOfTheWeek(TestCase):
    dw = DayOfTheWeek()

    def test_isleap__notleap(self):
        self.assertFalse(self.dw.isleap(1700))
        self.assertFalse(self.dw.isleap(1800))
        self.assertFalse(self.dw.isleap(1900))
        self.assertFalse(self.dw.isleap(2100))
        self.assertFalse(self.dw.isleap(2200))
        self.assertFalse(self.dw.isleap(2300))

    def test_isleap__leap(self):
        self.assertTrue(self.dw.isleap(1600))
        self.assertTrue(self.dw.isleap(2000))

    def test_day_of_the_week(self):
        self.assertEqual("Saturday", self.dw.dayOfTheWeek(1, 1, 1))
        self.assertEqual("Saturday", self.dw.dayOfTheWeek(31, 12, 1))
        self.assertEqual("Sunday", self.dw.dayOfTheWeek(1, 1, 2))

        self.assertEqual("Wednesday", self.dw.dayOfTheWeek(31, 12, 4))
        self.assertEqual("Thursday", self.dw.dayOfTheWeek(1, 1, 5))

        self.assertEqual("Tuesday", self.dw.dayOfTheWeek(31, 12, 20))

        # Bad
        self.assertEqual("Thursday", self.dw.dayOfTheWeek(31, 12, 100))

        # Bad
        #self.assertEqual("Friday", self.dw.dayOfTheWeek(31, 12, 101))

        # self.assertEqual("Friday", self.dw.dayOfTheWeek(31, 12, 1999))
        # self.assertEqual("Saturday", self.dw.dayOfTheWeek(1, 1, 2000))


        # self.assertEqual("Wednesday", self.dw.dayOfTheWeek(31, 12, 4))
        # self.assertEqual("Thursday", self.dw.dayOfTheWeek(1, 1, 5))
