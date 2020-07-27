from unittest import TestCase

from pyquiz.leetcode.MinStack import MinStack


class TestMinStack(TestCase):
    def test_min_top(self):
        ms = MinStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        self.assertEqual(-3, ms.getMin())  # return -3
        ms.pop()
        self.assertEqual(0, ms.top())  # return 0
        self.assertEqual(-2, ms.getMin())  # return -2

    def test_same_val(self):
        ms = MinStack()
        ms.push(1)
        ms.push(2)
        ms.push(2)
        ms.push(2)
        ms.pop()
        self.assertEqual(1, ms.getMin())
        self.assertEqual(2, ms.top())
        self.assertEqual(2, ms.pop())
        self.assertEqual(1, ms.getMin())
        self.assertEqual(2, ms.top())
        self.assertEqual(2, ms.pop())
        self.assertEqual(1, ms.getMin())
        self.assertEqual(1, ms.top())
        self.assertEqual(1, ms.pop())
        self.assertIsNone(ms.pop())
        self.assertIsNone(ms.getMin())
        self.assertIsNone(ms.top())

    def test_empty(self):
        ms = MinStack()
        self.assertIsNone(ms.getMin())
        self.assertIsNone(ms.top())
        self.assertIsNone(ms.pop())
        ms.push(1)
        ms.pop()
        self.assertIsNone(ms.getMin())
        self.assertIsNone(ms.top())
        self.assertIsNone(ms.pop())

    def test_badcase(self):
        ms = MinStack()
        ms.push(2)
        ms.push(0)
        ms.push(3)
        ms.push(0)
        self.assertEqual(0, ms.getMin())  # 2,0,3,0
        self.assertEqual(0, ms.pop())
        self.assertEqual(0, ms.getMin())  # 2,0,3
        self.assertEqual(3, ms.pop())
        self.assertEqual(0, ms.getMin())  # 2,0
        self.assertEqual(0, ms.pop())
        self.assertEqual(2, ms.getMin())  # 2
