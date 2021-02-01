from unittest import TestCase
from pyquiz.leetcode.SnapshotArray import SnapshotArray


class TestSnapshotArray(TestCase):

    def test_get_closest_snap_id__123_1(self):
        sa = SnapshotArray(1)
        self.assertEqual(1, sa.get_closest_snap_id([1, 2, 3], 1))

    def test_get_closest_snap_id__123_2(self):
        sa = SnapshotArray(1)
        self.assertEqual(2, sa.get_closest_snap_id([1, 2, 3], 2))

    def test_get_closest_snap_id__123_3(self):
        sa = SnapshotArray(1)
        self.assertEqual(3, sa.get_closest_snap_id([1, 2, 3], 3))

    def test_get_closest_snap_id__1_1(self):
        sa = SnapshotArray(1)
        self.assertEqual(1, sa.get_closest_snap_id([1], 1))

    def test_get_closest_snap_id__13_2(self):
        sa = SnapshotArray(1)
        self.assertEqual(1, sa.get_closest_snap_id([1, 3], 2))

    def test_get_closest_snap_id__13_4(self):
        sa = SnapshotArray(1)
        self.assertEqual(3, sa.get_closest_snap_id([1, 3], 4))

    def test_get_closest_snap_id__23_1(self):
        sa = SnapshotArray(1)
        self.assertEqual(None, sa.get_closest_snap_id([2, 3], 1))

    def test_get_closest_snap_id__12_1(self):
        sa = SnapshotArray(1)
        self.assertEqual(1, sa.get_closest_snap_id([1, 2], 1))

    def test_get_closest_snap_id__12_2(self):
        sa = SnapshotArray(1)
        self.assertEqual(2, sa.get_closest_snap_id([1, 2], 2))

    def test_example1(self):
        """
        Example 1:

        Input: ["SnapshotArray","set","snap","set","get"]
        [[3],[0,5],[],[0,6],[0,0]]
        Output: [null,null,0,null,5]
        Explanation:
        SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
        snapshotArr.set(0,5);  // Set array[0] = 5
        snapshotArr.snap();  // Take a snapshot, return snap_id = 0
        snapshotArr.set(0,6);
        snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

        :return:
        """
        # SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
        sa = SnapshotArray(3)

        # Set array[0] = 5
        sa.set(0, 5)

        # Take a snapshot, return snap_id = 0
        snapid = sa.snap()
        self.assertEqual(0, snapid)
        sa.set(0, 6)

        # Get the value of array[0] with snap_id = 0, return 5
        out = sa.get(0, 0)
        self.assertEqual(5, out)

    def test_case2(self):
        # SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
        sa = SnapshotArray(3)

        out = sa.get(2, 0)
        self.assertEqual(0, out)

        # Set array[0] = 5
        sa.set(0, 5)

        # Take a snapshot, return snap_id = 0
        snapid = sa.snap()
        self.assertEqual(0, snapid)

        sa.set(0, 6)

        snapid = sa.snap()
        self.assertEqual(1, snapid)

        out = sa.get(0, 0)
        self.assertEqual(5, out)

        out = sa.get(0, 1)
        self.assertEqual(6, out)

    def test_case3(self):
        """
        ["SnapshotArray","set","snap","snap","snap","get","snap","snap","get"]
        [[1],[0,15],[],[],[],[0,2],[],[],[0,0]]
        """
        sa = SnapshotArray(1)
        sa.set(0, 15)
        sa.snap()
        sa.snap()
        sa.snap()
        out = sa.get(0, 1)
        out = sa.get(0, 2)
        self.assertEqual(15, out)
        sa.snap()
        sa.snap()
        out = sa.get(0, 0)
        self.assertEqual(out, 15)

    def test_case4(self):
        """
        ["SnapshotArray","snap","get","get","set","get","set","get","set"]
        [[2],[],[1,0],[0,0],[1,8],[1,0],[0,20],[0,0],[0,7]]
        [null,0,0,0,null,8,null,20,null]
        Expected
        [null,0,0,0,null,0,null,0,null]
        """
        sa = SnapshotArray(2)
        self.assertEqual(0, sa.snap())
        self.assertEqual(0, sa.get(1, 0))
        self.assertEqual(0, sa.get(0, 0))
        sa.set(1, 8)
        self.assertEqual(0, sa.get(1, 0))
        sa.set(0, 20)
        self.assertEqual(0, sa.get(0, 0))
        sa.set(0, 7)

    def test_case5(self):
        """
        ["SnapshotArray","set","set","snap","get","set","snap","set","set","get","get"]
        [[3],[1,18],[1,4],[],[0,0],[0,20],[],[0,2],[1,1],[1,1],[1,0]]
        bad:        [null,null,null,0,0,null,1,null,null,0,4]
        Expected:   [null,null,null,0,0,null,1,null,null,4,4]
        """
        sa = SnapshotArray(3)
        # ["SnapshotArray","set","set","snap","get", "set","snap","set","set","get","get"]
        # [[3],[1,18],[1,4],[],[0,0], [0,20],[], [0,2],[1,1], [1,1],[1,0]]
        sa.set(1, 18)
        sa.set(1, 4)
        self.assertEqual(0, sa.snap())
        sa.set(0, 20)
        sa.snap()
        sa.set(0, 2)
        sa.set(1, 1)

        self.assertEqual(4, sa.get(1, 1))
        self.assertEqual(4, sa.get(1, 0))

    def test_case6(self):
        """
        ["SnapshotArray","set","snap","set","get","snap", "get","get","set","set", "snap","get","set","snap","snap","get","snap","get"]
        [[3],[1,5],[],[1,6],[0,0],[], [0,0],[0,0],[0,11],[1,16], [],[0,1],[2,12],[],[],[0,4],[],[1,1]]
        bad Output [null,null,0,null,0,1,0,0,null,null, 2,0,null,3,4,11,5,0]
        Expected   [null,null,0,null,0,1,0,0,null,null, 2,0,null,3,4,11,5,6]
        """
        sa = SnapshotArray(3)
        sa.set(1, 5)
        sa.snap()
        sa.set(1, 6)
        self.assertEqual(0, sa.get(0, 0))
        sa.snap()
        self.assertEqual(0, sa.get(0, 0))
        self.assertEqual(0, sa.get(0, 0))
        sa.set(0, 11)
        sa.set(1, 16)

    def test_case7(self):
        """
        ["SnapshotArray","snap","snap","set","snap","get","set","get","snap","get"]
        [[1],[],[],[0,4],[],[0,1],[0,12],[0,1],[],[0,3]]
        Output
        [null,0,1,null,2,0,null,0,3,0]
        Expected
        [null,0,1,null,2,0,null,0,3,12]
        """
        sa = SnapshotArray(1)
        sa.snap()
        sa.snap()
        sa.set(0, 4)
        sa.snap()
        self.assertEqual(0, sa.get(0, 1))
        sa.snap()
        self.assertEqual(0, sa.get(0, 0))
        self.assertEqual(0, sa.get(0, 0))
        sa.set(0, 11)
        sa.set(1, 16)

    def test_case7(self):
        sa = SnapshotArray(1)
        sa.snap()
        sa.snap()
        sa.set(0,4)
        sa.snap()
        sa.get(0,1)
        sa.get(0,12)
        sa.set(0,1)
        sa.snap()
        sa.get(0,3)
#
#
#         ["SnapshotArray","snap","snap","set","snap","get","set","get","snap","get"]
# [[1],[],[],[0,4],[],[0,1],[0,12],[0,1],[],[0,3]]
