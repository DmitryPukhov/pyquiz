from unittest import TestCase
from pyzuiz.ctci.arraysandstrings.PalindromePermutation import PalindromePermutation


class TestPalindromePermutation(TestCase):
    def test_is_permutation_true(self):
        assert PalindromePermutation().is_permutation("aba")
        assert PalindromePermutation().is_permutation("abba")
        assert PalindromePermutation().is_permutation("abbac")

    def test_is_permutation_false(self):
        assert ~PalindromePermutation().is_permutation("abaa")
        assert ~PalindromePermutation().is_permutation("abca")
