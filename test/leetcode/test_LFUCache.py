from unittest import TestCase

from pyquiz.leetcode.LFUCache import LFUCache


class TestLFUCache(TestCase):
    def test_example1(self):
        """
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
        """
        lfu = LFUCache(2);
        lfu.put(1, 1);
        lfu.put(2, 2);

        out = lfu.get(1);
        self.assertEqual(1, out)  # Return 1

        # evicts key 2
        lfu.put(3, 3);
        out = lfu.get(2);  # return -1 (not found)
        self.assertEqual(-1, out)
        out = lfu.get(3);  # return 3
        self.assertEqual(3, out)
        lfu.put(4, 4);  # evicts key 1.
        out = lfu.get(1);  # return -1 (not found)
        self.assertEqual(-1, out)
        out = lfu.get(3);  # return 3
        self.assertEqual(3, out)
        out = lfu.get(4);  # return 4
        self.assertEqual(4, out)

    def test_get_empty(self):
        lfu = LFUCache(0);
        lfu.put(1,1)
        self.assertEqual(-1, lfu.get(1))

    def test_put(self):
        lfu = LFUCache(1)
        lfu.put(1, 1)
        self.assertEqual(1, lfu.get(1))

    def test_equal_items(self):
        lfu = LFUCache(2);
        lfu.put(1, 1);
        self.assertEqual(1, lfu.get(1))
        lfu.put(2, 2);
        self.assertEqual(2, lfu.get(2))
        lfu.put(3, 3);

        out = lfu.get(1);
        self.assertEqual(-1, out)  # Return 1
        out = lfu.get(2);
        self.assertEqual(2, out)  # Return 1
        out = lfu.get(3);
        self.assertEqual(3, out)  # Return 1

    def test_freq(self):
        lfu = LFUCache(2);
        # 1 cnt = 3
        lfu.put(1, 1);
        self.assertEqual(1, lfu.get(1))
        lfu.get(1)
        # 2 cnt = 3
        lfu.put(2, 2);
        lfu.get(2)
        self.assertEqual(2, lfu.get(2))

        lfu.get(2)
        lfu.get(1)

        # 3 evicts 2
        lfu.put(3, 3);
        self.assertEqual(-1, lfu.get(2))

    def test_sample1(self):
        lfu = LFUCache(2)
        lfu.put(1,1)
        lfu.put(2,2)
        lfu.get(1)
        lfu.put(3,3)
        lfu.get(2)
        lfu.get(3)
        lfu.put(4,4)
        lfu.get(1)
        lfu.get(3)
        lfu.get(4)
        lfu.put(1,1)
        lfu.put(2,2)
        lfu.get(1)
        lfu.put(3,3)
        self.assertEqual(2,lfu.get(2))

# ["LFUCache","put","put","get","put","get","get","put","get","get","get","put","put","get","put","get","get","put","get","get","get","put","put","get","put","get","get","put","get","get","get"]
# [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]

