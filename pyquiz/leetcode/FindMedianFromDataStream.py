import heapq
import unittest


class MedianFinder_nlogn:
    """
    Find Median from Data Stream
    The median is the middle value in an ordered integer list.
    If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

    Constraints:

    -105 <= num <= 105
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.

    Follow up:
    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []
        self.len = 0

    def addNum(self, num: int) -> None:
        self.values.append(num)
        self.len += 1

    def findMedian(self) -> float:
        self.values.sort()
        if not self.values:
            return None
        if self.len == 1:
            return self.values[0]
        if self.len % 2 == 1:
            return self.values[self.len // 2]
        else:
            return self.values[self.len // 2] / 2 + self.values[self.len // 2 - 1] / 2


class MedianFinder:
    """
    Find Median from Data Stream
    The median is the middle value in an ordered integer list.
    If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

    Constraints:

    -105 <= num <= 105
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.

    Follow up:
    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minheap = []
        self.maxheap = []
        self.minheaplen = 0
        self.maxheaplen = 0

    def addNum(self, num: int) -> None:
        # Initial case = minheap or maxheap are empty
        if not self.maxheap:
            # Push very first item to left part
            heapq.heappush(self.maxheap, -num)
            self.maxheaplen += 1
        elif not self.minheap:
            # Push second item to right part
            heapq.heappush(self.minheap, num)
            self.minheaplen += 1
        else:
            # Push 3rd and further item to a proper heap
            # [1] [3]  + 2 => [1,2] => 3
            # [1,2], [4] + 3 => [1,2], [3,4]
            # [1,3], [4] + 2 => [1,2], [3,4]
            if self.maxheaplen == self.minheaplen + 1:
                # Left part shold not be longer than right part +1
                # So add to right part
                heapq.heappush(self.minheap, num)
                self.minheaplen += 1
            else:
                heapq.heappush(self.maxheap, -num)
                self.maxheaplen += 1
        self.balance()

    def balance(self):
        """
        Balance heaps: max heap len = min heap len or max heap len = min heap len + 1
        max heap head <= min heap head
        """
        while self.minheaplen > self.maxheaplen + 1:
            # Move from left to right
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            self.minheaplen -= 1
            self.maxheaplen += 1
        while self.maxheap and self.minheap and self.minheap[0] < -self.maxheap[0]:
            # Swap left and right
            l=-heapq.heappop(self.maxheap)
            r = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -r)
            heapq.heappush(self.minheap, l)

    def findMedian(self) -> float:
        if not self.maxheap:
            # Empty data
            return None
        elif not self.minheap:
            # Single element should be in left heap
            return -self.maxheap[0]
        else:
            # Here min heap and max heap exist
            if self.minheaplen == self.maxheaplen:
                return -self.maxheap[0] / 2 + self.minheap[0] / 2
            else:
                return -self.maxheap[0]


class TestMedianFinder(unittest.TestCase):
    def test_leetcodecase1(self):
        mf = MedianFinder()
        mf.addNum(6)
        mf.addNum(10)
        mf.addNum(2)
        self.assertEqual(6, mf.findMedian())
        mf.addNum(6)
        mf.addNum(5)
        mf.addNum(0)
        mf.addNum(6)
        mf.addNum(3)
        mf.addNum(1)
        mf.addNum(0)
        mf.addNum(0)
        mf.findMedian()

    def test_stress(self):
        mf = MedianFinder()
        for i in range(10000):
            mf.addNum(i)
            self.assertIsNotNone(mf.findMedian())

    def test_12345(self):
        mf = MedianFinder()
        mf.addNum(2)
        mf.addNum(1)
        mf.addNum(5)
        mf.addNum(4)
        mf.addNum(3)
        self.assertEqual(3, mf.findMedian())

    def test_41332(self):
        mf = MedianFinder()
        mf.addNum(4)
        mf.addNum(1)
        mf.addNum(3)
        mf.addNum(2)
        self.assertEqual(2.5, mf.findMedian())

    def test_1(self):
        mf = MedianFinder()
        mf.addNum(1)
        self.assertEqual(1, mf.findMedian())

    def test_13(self):
        mf = MedianFinder()
        mf.addNum(1)
        mf.addNum(3)
        self.assertEqual(2, mf.findMedian())

    def test_123(self):
        mf = MedianFinder()
        mf.addNum(2)
        mf.addNum(3)
        mf.addNum(1)
        self.assertEqual(2, mf.findMedian())

    def test_example1(self):
        """
        Example 1:
        Input
        ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
        [[], [1], [2], [], [3], []]
        Output
        [null, null, null, 1.5, null, 2.0]

        Explanation
        MedianFinder medianFinder = new MedianFinder();
        medianFinder.addNum(1);    // arr = [1]
        medianFinder.addNum(2);    // arr = [1, 2]
        medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
        medianFinder.addNum(3);    // arr[1, 2, 3]
        medianFinder.findMedian(); // return 2.0
        """
        mf = MedianFinder()
        mf.addNum(3)
        mf.addNum(1)
        self.assertEqual(2.0, mf.findMedian())
        mf.addNum(2)
        self.assertEqual(2.0, mf.findMedian())
