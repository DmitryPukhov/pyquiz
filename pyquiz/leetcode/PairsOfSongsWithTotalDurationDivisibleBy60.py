from collections import defaultdict
from typing import List, Counter
from unittest import TestCase


class Solution:
    """
    1010. Pairs of Songs With Total Durations Divisible by 60
    You are given a list of songs where the ith song has a duration of time[i] seconds.
    Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
    Formally, we want the number of indices i, j such that i < j with (time[i] + time[j]) % 60 == 0.

    Constraints:
    1 <= time.length <= 6 * 104
    1 <= time[i] <= 500
    """

    def num_pairs_divisible_by_60(self, time: List[int]) -> int:
        # 30,20,150,100,140
        # 30 + 150
        if not time:
            return 0
        counts = defaultdict(int)
        out = 0
        for t in time:
            tt = t % 60
            pair = (60 - tt) % 60
            out += counts[pair]
            counts[tt] += 1

        return out


class TestSolution(TestCase):
    def test_num_pairs_example1(self):
        """
        Example 1:
        Input: time = [30,20,150,100,40]
        Output: 3
        Explanation: Three pairs have a total duration divisible by 60:
        (time[0] = 30, time[2] = 150): total duration 180
        (time[1] = 20, time[3] = 100): total duration 120
        (time[1] = 20, time[4] = 40): total duration 60
        """
        self.assertEqual(3, Solution().num_pairs_divisible_by_60(time=[30, 20, 150, 100, 40]))

    def test_num_pairs_example2(self):
        """
        Example 2:
        Input: time = [60,60,60]
        Output: 3
        Explanation: All three pairs have a total duration of 120, which is divisible by 60.
        """
        self.assertEqual(3, Solution().num_pairs_divisible_by_60(time=[60, 60, 60]))
