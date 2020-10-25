from unittest import TestCase

from pyquiz.leetcode.KthLargestElement import KthLargestElement


class TestKthLargestElement(TestCase):
    def test_find_kth_largest__321564_2(self):
        """
        Example 1:
        Input: [3,2,1,5,6,4] and k = 2
        Output: 5
        """
        res = KthLargestElement().findKthLargest([3, 2, 1, 5, 6, 4], 2)
        self.assertEqual(5, res)

    def test_find_kth_largest__323124556_4(self):
        """
        Example 2:
        Input: [3,2,3,1,2,4,5,5,6] and k = 4
        Output: 4
        """
        res = KthLargestElement().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
        self.assertEqual(4, res)

    def test_find_kth_largest__1_1(self):
        res = KthLargestElement().findKthLargest([1], 1)
        self.assertEqual(1, res)

    def test_find_kth_largest__123_2(self):
        res = KthLargestElement().findKthLargest([1,2,3], 2)
        self.assertEqual(2, res)

    def test_find_kth_largest__321_2(self):
        res = KthLargestElement().findKthLargest([3,2,1], 2)
        self.assertEqual(2, res)

    def test_find_kth_largest__213_2(self):
        res = KthLargestElement().findKthLargest([2,1,3], 2)
        self.assertEqual(2, res)

    def test_find_kth_largest__neg1neg1_2(self):
        res = KthLargestElement().findKthLargest([-1,-1], 2)
        self.assertEqual(-1, res)

    def test_partition__312_0(self):
        nums = [3,1,2]
        pivot = 0
        pivot = KthLargestElement()._partition(nums, 0, len(nums)-1,pivot)
        self.assertEqual(nums[pivot],3)
        self.assertTrue(max(nums[:pivot]) < nums[pivot])

    def test_partition__312_2(self):
        nums = [3,1,2]
        pivot = 1
        pivot = KthLargestElement()._partition(nums, 0, len(nums)-1,pivot)
        self.assertEqual(nums[pivot],1)
        self.assertTrue(min(nums[pivot+1:]) > nums[pivot])

    def test_partition__321_1(self):
        nums = [3,2,1]
        pivot = 1
        pivot = KthLargestElement()._partition(nums, 0, len(nums)-1,pivot)
        self.assertEqual(nums[pivot],2)
        self.assertTrue(max(nums[:pivot]) < nums[pivot])
