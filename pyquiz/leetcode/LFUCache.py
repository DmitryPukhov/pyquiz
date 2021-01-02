import heapq
from collections import defaultdict, OrderedDict
from queue import PriorityQueue


class LFUCache:
    """
    Design and implement a data structure for Least Frequently Used (LFU) cache.
    Implement the LFUCache class:

    LFUCache(int capacity) Initializes the object with the capacity of the data structure.
    int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
    void put(int key, int value) Sets or inserts the value if the key is not already present.
    When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
    For this problem, when there is a tie (i.e., two or more keys with the same frequency),
    the least recently used key would be evicted. Notice that the number of times an item is used is the number
    of calls to the get and put functions for that item
    since it was inserted. This number is set to zero when the item is removed.

    Example 1:
    Input
    ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
    Output
    [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

    Explanation
    LFUCache lfu = new LFUCache(2);
    lfu.put(1, 1);
    lfu.put(2, 2);
    lfu.get(1);      // return 1
    lfu.put(3, 3);   // evicts key 2
    lfu.get(2);      // return -1 (not found)
    lfu.get(3);      // return 3
    lfu.put(4, 4);   // evicts key 1.
    lfu.get(1);      // return -1 (not found)
    lfu.get(3);      // return 3
    lfu.get(4);      // return 4


    Constraints:

    0 <= capacity, key, value <= 104
    At most 105 calls will be made to get and put.
    """

    def __init__(self, capacity: int):
        # Use map and heap
        self._capacity = capacity
        self._map = dict()
        self._cntheap = []
        self._time = 0

    def get(self, key: int) -> int:
        self._time += 1

        if key not in self._map:
            return -1
        value, prevcnt = self._map[key]

        # Update map, push to heap
        self._map[key] = (value, prevcnt + 1)
        heapq.heappush(self._cntheap, (prevcnt + 1, self._time, key))
        return value

    def put(self, key: int, value: int) -> None:
        self._time += 1
        # If capacity will not be out of
        if len(self._map) >= self._capacity and key not in self._map:
            self.clear()
        if self._capacity == 0:
            return

        if key not in self._map:
            self._map[key] = (value, 1)
            heapq.heappush(self._cntheap, (1, self._time, key))
        else:
            prevcnt = self._map[key][1]
            # Update map, push to heap
            self._map[key] = (value, prevcnt + 1)
            heapq.heappush(self._cntheap, (prevcnt + 1, self._time, key))

    def clear(self):
        """
        Clear least frequently used item
        """
        if not self._map:
            return
        cnt, _, key = heapq.heappop(self._cntheap)
        while (key not in self._map) or self._map[key][1] != cnt:
            (cnt, _, key) = heapq.heappop(self._cntheap)
        self._map.pop(key)
