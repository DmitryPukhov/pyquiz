from unittest import TestCase

from pyzuiz.ctci.arraysandstrings import OneAway


class TestOneAway(TestCase):

    def test_is_one_away__empty__one_away(self):
        assert OneAway().is_one_away('', '')
        assert OneAway().is_one_away('1', '')

    def test_is_one_away__reps_chars__one_away(self):
        assert not OneAway().is_one_away('12222', '122')

    def test_is_one_away__equal_strings__one_away(self):
        assert OneAway().is_one_away('123', '123')

    def test_is_one_away__single_chars__one_away(self):
        assert OneAway().is_one_away('1', '2')

    def test_is_one_away__two_chars__one_away(self):
        assert OneAway().is_one_away('12', '13')

    def test_is_one_away__replace_in_middle__one_away(self):
        assert OneAway().is_one_away('213', '223')
