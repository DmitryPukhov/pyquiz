from unittest import TestCase

from pyquiz.leetcode.NextPermutation import NextPermutation


class TestNextPermutation(TestCase):

    def test_next_permutation__21(self):
        nums = [2,1]
        NextPermutation().nextPermutation(nums)
        self.assertEqual([1,2], nums)

    def test_next_permutation__12(self):
        nums = [1,2]
        NextPermutation().nextPermutation(nums)
        self.assertEqual([2,1], nums)

    def test_next_permutation__1(self):
        nums = [1]
        NextPermutation().nextPermutation(nums)
        self.assertEqual([1], nums)

    def test_next_permutation__empty(self):
        nums = []
        NextPermutation().nextPermutation(nums)
        self.assertEqual([], nums)

    def test_next_permutation__123(self):
        ## 1,2,3 → 1,3,2
        nums = [1, 2, 3]
        NextPermutation().nextPermutation(nums)
        self.assertEqual([1, 3, 2], nums)

    def test_next_permutation__132(self):
        ## 1,2,3 → 1,3,2
        nums = [1, 3, 2]
        NextPermutation().nextPermutation(nums)
        self.assertEqual([2, 1, 3], nums)

    def test_next_permutation__321(self):
        # 3,2,1 → 1,2,3
        nums = [3, 2, 1]
        NextPermutation().nextPermutation(nums)
        self.assertEqual([1, 2, 3], nums)

    def test_next_permutation__115(self):
        # 1,1,5 → 1,5,1
        nums = [1, 1, 5]
        NextPermutation().nextPermutation(nums)
        self.assertEqual([1, 5, 1], nums)

    def test_next_permutation__1231(self):
        # 1,2,3,1 → 1,3,2,1
        nums = [1, 2, 3, 1]
        NextPermutation().nextPermutation(nums)
        self.assertEqual([1, 3, 1, 2], nums)
