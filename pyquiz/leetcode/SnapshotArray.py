from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import OrderedDict, List


class SnapshotArray:
    """
    Implement a SnapshotArray that supports the following interface:

    SnapshotArray(int length) initializes an array-like data structure with the given length.  Initially, each element equals 0.
    void set(index, val) sets the element at the given index to be equal to val.
    int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
    int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id


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

    Constraints:
    1 <= length <= 50000
    At most 50000 calls will be made to set, snap, and get.
    0 <= index < length
    0 <= snap_id < (the total number of times we call snap())
    0 <= val <= 10^9
    """

    def __init__(self, length: int):
        self.items = defaultdict(OrderedDict)
        self.snapid = 0

    def set(self, index: int, val: int) -> None:
        self.items[index][self.snapid] = val

    def snap(self) -> int:
        self.snapid += 1
        return self.snapid - 1

    def get(self, index: int, snap_id: int) -> int:
        itemsnaps = self.items[index]
        if not itemsnaps:
            return 0

        closest_snap_id = self.get_closest_snap_id(list(itemsnaps.keys()), snap_id)

        return itemsnaps[closest_snap_id] if closest_snap_id is not None else 0

    def get_closest_snap_id(self, items: List[int], x: int):
        """
        Logic similar to bisect_right in python.
        """
        if not items or items[0] > x:
            return None
        lo = 0
        hi = len(items) - 1
        index = -1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if items[mid] == x:
                index = mid
                break
            if items[mid] >= x:
                index = mid
                hi = mid - 1
            else:
                index = lo
                lo = mid + 1
        if items[hi] <= x: index = hi
        return items[index] if index >= 0 else None

# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
