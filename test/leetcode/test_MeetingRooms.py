from unittest import TestCase

from pyquiz.leetcode.MeetingRooms import MeetingRooms


class TestMeetingRooms(TestCase):
    def test_min_meeting_rooms__0_30__5_10__15_20(self):
        """
        Example 1:
        Input: [[0, 30],[5, 10],[15, 20]]
        Output: 2
        """
        res = MeetingRooms().minMeetingRooms([[0, 30], [5, 10], [15, 20]])
        self.assertEqual(2, res)

    def test_min_meeting_rooms__7_10__2_4(self):
        """
        Example 2:
        Input: [[7,10],[2,4]]
        Output: 1
        """
        res = MeetingRooms().minMeetingRooms([[7,10],[2,4]])
        self.assertEqual(1, res)

    def test_min_meeting_room__26_29__19_26__19_28__4_19__4_25(self):
        #[[26,29],[19,26],[19,28],[4,19],[4,25]]
        res = MeetingRooms().minMeetingRooms([[26,29],[19,26],[19,28],[4,19],[4,25]])
        self.assertEqual(3, res)
