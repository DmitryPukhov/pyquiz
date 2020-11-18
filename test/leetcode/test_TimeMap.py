from unittest import TestCase

from pyquiz.leetcode.TimeMap import TimeMap


class TestTimeMap(TestCase):
    def test_example1(self):
        """
        Example 1:

        Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
        Output: [null,null,"bar","bar",null,"bar2","bar2"]
        Explanation:
        TimeMap kv;
        kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with timestamp = 1
        kv.get("foo", 1);  // output "bar"
        kv.get("foo", 3); // output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
        kv.set("foo", "bar2", 4);
        kv.get("foo", 4); // output "bar2"
        kv.get("foo", 5); //output "bar2"

        """
        kv = TimeMap()
        kv.set("foo", "bar", 1);  # store the key "foo" and value "bar" along with timestamp = 1
        self.assertEqual("bar", kv.get("foo", 1))  # output "bar"
        self.assertEqual("bar", kv.get("foo", 3))  # output "bar" since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie "bar"
        kv.set("foo", "bar2", 4);
        self.assertEqual("bar2", kv.get("foo", 4))
        self.assertEqual("bar2", kv.get("foo", 5))

    def test_example2(self):
        """
        Example 2:

        Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
        Output: [null,null,null,"","high","high","low","low"]
        """
        kv = TimeMap()
        kv.set("love", "high", 10)
        kv.set("love", "low", 20)

        self.assertEqual("", kv.get("love", 5))
        self.assertEqual("high", kv.get("love", 10))
        self.assertEqual("high", kv.get("love", 15))
        self.assertEqual("low", kv.get("love", 20))
        self.assertEqual("low", kv.get("love", 25))

    def test_empty(self):
        kv = TimeMap()
        self.assertEqual(None, kv.get("key1", 5))

    def test_empty_key(self):
        kv = TimeMap()
        kv.set("key1", "val1", 20)
        self.assertEqual(None, kv.get("key2", 5))