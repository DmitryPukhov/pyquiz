from unittest import TestCase

from pyquiz.leetcode.TopKFrequentElements import TopKFrequentElements


class TestTopKFrequentElements(TestCase):
    def test_top_kfrequent__example1(self):
        """
        Example 1:
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        """
        out = TopKFrequentElements().topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2)
        self.assertEqual([1, 2], out)

    def test_top_kfrequent__example2(self):
        """
        Example 2:
        Input: nums = [1], k = 1
        Output: [1]
        """
        out = TopKFrequentElements().topKFrequent(nums=[1], k=1)
        self.assertEqual([1], out)

    def test_top_kfrequent__neg1(self):
        out = TopKFrequentElements().topKFrequent(nums=[-1, -1], k=1)
        self.assertEqual([-1], out)

    def test_top_kfrequent__12(self):
        out = TopKFrequentElements().topKFrequent(nums=[1, 2], k=2)
        self.assertEqual([1, 2], out)

    def test_top_kfrequent__41neg12neg123(self):
        out = TopKFrequentElements().topKFrequent(nums=[4, 1, -1, 2, -1, 2, 3], k=2)
        self.assertEqual([-1, 2], out)
