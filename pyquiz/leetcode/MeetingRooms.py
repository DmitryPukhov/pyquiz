import collections
from collections import Counter
from typing import List


class MeetingRooms:
    """
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
    find the minimum number of conference rooms required.

    Example 1:
    Input: [[0, 30],[5, 10],[15, 20]]
    Output: 2

    Example 2:
    Input: [[7,10],[2,4]]
    Output: 1
    """

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        #intervals = [sorted([interval[0], max(interval[0], interval[1])]) for interval in intervals]
        #zerointervals = [interval for interval in intervals if interval[0] == interval[1]]
        # Number of rooms by start or end time
        startcounts = collections.Counter([interval[0] for interval in intervals])
        endcounts = collections.Counter([interval[1] for interval in intervals])
        #zerocounts = collections.Counter([interval[0] for interval in zerointervals])
        # Start and end times
        moments = sorted(set(startcounts.keys()) | set(endcounts.keys()))

        currooms = maxrooms = 0
        for t in moments:
            currooms += startcounts.get(t, 0)
            currooms -= endcounts.get(t, 0)
            maxrooms = max(currooms, maxrooms)
            #zerorooms = zerocounts.get(t, 0)
            # maxrooms = max(currooms + zerorooms, maxrooms)
        return maxrooms
