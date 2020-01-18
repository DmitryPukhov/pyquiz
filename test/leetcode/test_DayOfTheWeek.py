from unittest import TestCase

from pyzuiz.leetcode.DayOfTheWeek import DayOfTheWeek


class TestDayOfTheWeek(TestCase):
    dw = DayOfTheWeek()

    def test_leaps(self):
        # Test how many leaps passed since 1972
        self.assertEqual(0, self.dw.leaps(1971))
        self.assertEqual(0, self.dw.leaps(1972))
        self.assertEqual(1, self.dw.leaps(1973))

        self.assertEqual(2, self.dw.leaps(1977))
        self.assertEqual(3, self.dw.leaps(1981))
        self.assertEqual(4, self.dw.leaps(1985))
        self.assertEqual(5, self.dw.leaps(1989))
        self.assertEqual(6, self.dw.leaps(1993))
        self.assertEqual(7, self.dw.leaps(1997))
        self.assertEqual(8, self.dw.leaps(2001))
        self.assertEqual(9, self.dw.leaps(2005))
        self.assertEqual(10, self.dw.leaps(2009))
        self.assertEqual(11, self.dw.leaps(2013))

    def test_isleap(self):
        self.assertFalse(self.dw.isleap(1971))
        self.assertTrue(self.dw.isleap(1972))
        self.assertTrue(self.dw.isleap(2000))
        self.assertFalse(self.dw.isleap(2100))
        self.assertTrue(self.dw.isleap(2400))

    def test_day_of_the_week(self):
        self.assertEqual("Friday", self.dw.dayOfTheWeek(1, 1, 1971))
        self.assertEqual("Saturday", self.dw.dayOfTheWeek(1, 1, 1972))
        self.assertEqual("Tuesday", self.dw.dayOfTheWeek(29, 2, 1972))
        self.assertEqual("Wednesday", self.dw.dayOfTheWeek(1, 3, 1972))
        self.assertEqual("Sunday", self.dw.dayOfTheWeek(31, 12, 1972))
        self.assertEqual("Monday", self.dw.dayOfTheWeek(1, 1, 1973))
        self.assertEqual("Friday", self.dw.dayOfTheWeek(31, 12, 1999))
        self.assertEqual("Saturday", self.dw.dayOfTheWeek(1, 1, 2000))
        self.assertEqual("Sunday", self.dw.dayOfTheWeek(31, 12, 2000))
        self.assertEqual("Monday", self.dw.dayOfTheWeek(1, 1, 2001))
        self.assertEqual("Saturday", self.dw.dayOfTheWeek(18, 1, 2020))

        self.assertEqual("Saturday", self.dw.dayOfTheWeek(31, 12, 2067))

        self.assertEqual("Monday", self.dw.dayOfTheWeek(31, 12, 2068))
        self.assertEqual("Tuesday", self.dw.dayOfTheWeek(1, 1, 2069))
