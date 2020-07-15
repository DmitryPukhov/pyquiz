from unittest import TestCase

from pyquiz.leetcode.VerifyingAlienDictionary import VeryfyingAlienDictionary


class TestVeryfyingAlienDictionary(TestCase):

    def test_is_alien_sorted__hello_leetcode(self):
        res = VeryfyingAlienDictionary().isAlienSorted(
            words=["hello", "leetcode"],
            order="hlabcdefgijkmnopqrstuvwxyz")
        self.assertTrue(res)

    def test_is_alien_sorted__word_world(self):
        res = VeryfyingAlienDictionary().isAlienSorted(
            words=["word", "world", "row"],
            order="worldabcefghijkmnpqstuvxyz")
        self.assertFalse(res)

    def test_is_alien_sorted__apple_app(self):
        res = VeryfyingAlienDictionary().isAlienSorted(
            words=["apple", "app"],
            order="abcdefghijklmnopqrstuvwxyz")
        self.assertFalse(res)

    def test_is_alien_sorted_empty(self):
        res = VeryfyingAlienDictionary().isAlienSorted(
            words=[],
            order="")
        self.assertTrue(res)

    def test_is_alien_sorted_nones(self):
        res = VeryfyingAlienDictionary().isAlienSorted(
            words=None,
            order=None)
        self.assertTrue(res)
