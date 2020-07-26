from unittest import TestCase

from pyquiz.leetcode.MyHashMap import MyHashMap


class TestMyHashMap(TestCase):
    def test_put_get_remove(self):
        hm = MyHashMap()
        hm.put(1, 10)
        hm.put(2, 20)
        self.assertEqual(10, hm.get(1))
        self.assertEqual(-1, hm.get(3))
        hm.put(2, 200)
        self.assertEqual(200, hm.get(2))
        hm.remove(2)
        self.assertEqual(-1, hm.get(2))

    def test_empty(self):
        hm = MyHashMap()
        self.assertEqual(-1, hm.get(1))
        hm.remove(1)
        self.assertEqual(-1, hm.get(1))
        hm.put(1, 1)
        hm.remove(1)
        self.assertEqual(-1, hm.get(1))

    def test_multiput(self):
        hm = MyHashMap()
        hm.put(1, 1)
        hm.put(1, 1)
        hm.remove(1)
        self.assertEqual(-1, hm.get(1))

    def test_multiremove(self):
        hm = MyHashMap()
        hm.remove(1)
        hm.remove(1)
        hm.put(1, 1)
        hm.remove(1)
        hm.remove(1)
        hm.remove(1)
        hm.remove(1)
        self.assertEqual(-1, hm.get(1))
        hm.put(1, 1)
        self.assertEqual(1, hm.get(1))
