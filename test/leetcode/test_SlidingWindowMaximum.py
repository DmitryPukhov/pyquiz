from unittest import TestCase
from pyquiz.leetcode.SlidingWindowMaximum import Solution


class TestSolution(TestCase):

    def test_max_sliding_window__example1(self):
        """
        Example 1:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]
        Explanation:
        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7
        """
        out = Solution().maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3)
        self.assertEqual([3, 3, 5, 5, 6, 7], out)

    def test_max_sliding_window__example2(self):
        """
        Example 2:
        Input: nums = [1], k = 1
        Output: [1]
        """
        out = Solution().maxSlidingWindow(nums=[1], k=1)
        self.assertEqual([1], out)

    def test_max_sliding_window__example3(self):
        """
        Example 3:
        Input: nums = [1,-1], k = 1
        Output: [1,-1]
        """
        out = Solution().maxSlidingWindow(nums=[1, -1], k=1)
        self.assertEqual([1, -1], out)

    def test_max_sliding_window__example4(self):
        """
        Example 4:
        Input: nums = [9,11], k = 2
        Output: [11]
        """
        out = Solution().maxSlidingWindow(nums=[9, 11], k=2)
        self.assertEqual([11], out)

    def test_max_sliding_window__example5(self):
        """
        Input: nums = [4,-2], k = 2
        Output: [4]
        """
        out = Solution().maxSlidingWindow(nums=[4, -2], k=2)
        self.assertEqual([4], out)

    def test_max_sliding_window__543_2(self):
        out = Solution().maxSlidingWindow(nums=[5,4,3], k=2)
        self.assertEqual([5,4], out)
