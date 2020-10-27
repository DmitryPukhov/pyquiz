from unittest import TestCase

from pyquiz.leetcode.SearchInRotatedArray import SearchInRotatedArray


class TestSearchInRotatedArray(TestCase):

    def test_search__neg2neg112345_neg1(self):
        self.assertEqual(1, SearchInRotatedArray().search(nums=[-2,-1,1,2,3,4,5], target=-1))

    def test_search__561234_6(self):
        self.assertEqual(0, SearchInRotatedArray().search(nums=[6,7,1,2,3,4,5], target=6))

    def test_search__561234_7(self):
        self.assertEqual(1, SearchInRotatedArray().search(nums=[6,7,1,2,3,4,5], target=7))


    def test_search__561234_2(self):
        self.assertEqual(3, SearchInRotatedArray().search(nums=[5,6,1,2,3,4], target=2))

    def test_search__4567012_4(self):
        """
        Example 1:
        Input: nums = [4,5,6,7,0,1,2], target = 0
        Output: 4
        """
        self.assertEqual(4, SearchInRotatedArray().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0))

    def test_search__4467012_3(self):
        """
        Example 2:
        Input: nums = [4,5,6,7,0,1,2], target = 3
        Output: -1
        """
        self.assertEqual(-1, SearchInRotatedArray().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3))

    def test_search__1_0(self):
        """
        Example 3:
        Input: nums = [1], target = 0
        Output: -1
        :return:
        """
        self.assertEqual(-1, SearchInRotatedArray().search(nums=[1], target=0))

    def test_search_pivot__4567012(self):
        self.assertEqual(4, SearchInRotatedArray()._search_pivot([4, 5, 6, 7, 0, 1, 2]))

    def test_search_pivot__1_0(self):
        self.assertEqual(0, SearchInRotatedArray()._search_pivot([1]))

    def test_search_pivot__21_0(self):
        self.assertEqual(1, SearchInRotatedArray()._search_pivot([2,1]))

    def test_search_pivot__312_1(self):
        self.assertEqual(1, SearchInRotatedArray()._search_pivot([3,1,2]))

    def test_search_pivot__123_0(self):
        self.assertEqual(0, SearchInRotatedArray()._search_pivot([1,2,3]))

    def test_search_pivot__231_0(self):
        self.assertEqual(2, SearchInRotatedArray()._search_pivot([2,3,1]))

    def test_search_subarray__123_1(self):
        self.assertEqual(0, SearchInRotatedArray()._search_subarray([1,2,3],1,0,2))

    def test_search_subarray__1234_1_0_2(self):
        self.assertEqual(0, SearchInRotatedArray()._search_subarray([1,2,3,4],1,0,2))

    def test_search_subarray__1234_1_1_2(self):
        self.assertEqual(-1, SearchInRotatedArray()._search_subarray([1,2,3,4],1,1,2))
