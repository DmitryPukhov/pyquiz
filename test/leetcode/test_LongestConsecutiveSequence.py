from unittest import TestCase

from pyquiz.leetcode.LongestConsecutiveSequence import LongestConsecutiveSequence


class TestLongestConsecutiveSequence(TestCase):
    def test_longest_consecutive__example1(self):
        """
        Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
        """
        res = LongestConsecutiveSequence().longestConsecutive([100, 4, 200, 1, 3, 2])
        self.assertEqual(4, res)

    def test_longest_consecutive__example2(self):
        """
        Example 2:
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9
        """
        res = LongestConsecutiveSequence().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
        self.assertEqual(9, res)

    def test_longest_consecutive__111(self):
        res = LongestConsecutiveSequence().longestConsecutive([1, 1, 1])
        self.assertEqual(1,res)

    def test_longest_consecutive__111(self):
        res = LongestConsecutiveSequence().longestConsecutive([1, 2, 2,3,1,1])
        self.assertEqual(3,res)

    def test_longest_consecutive__empty(self):
        res = LongestConsecutiveSequence().longestConsecutive([])
        self.assertEqual(0,res)
