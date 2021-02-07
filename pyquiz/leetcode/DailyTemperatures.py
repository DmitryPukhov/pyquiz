from typing import List


class Solution:
    """
    Daily Temperatures
    Given a list of daily temperatures T, return a list such that, for each day in the input,
    tells you how many days you would have to wait until a warmer temperature.
    If there is no future day for which this is possible, put 0 instead.

    For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
    your output should be [1, 1, 4, 2, 1, 1, 0, 0].

    Note: The length of temperatures will be in the range [1, 30000].
    Each temperature will be an integer in the range [30, 100].
    """

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        daysleft = [0] * len(T)
        for i in range(len(T) - 1, -1, -1):
            self.__daysleft(T, daysleft, i)
        return daysleft

    def __daysleft(self, t: List[int], dl: List[int], i: int):
        """
        How many days left until warmer temperature
        """
        if i >= len(t) - 1:
            # The last day, no future
            dl[i] = 0
            return

        j = i + 1
        while j < len(t) and t[j] <= t[i] and dl[j] > 0:
            j += dl[j]
        # If got warmer day, set it to days left array
        dl[i] = j - i if j < len(dl) and t[j] > t[i] else 0
