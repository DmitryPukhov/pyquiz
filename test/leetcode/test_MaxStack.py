from unittest import TestCase

from pyquiz.leetcode.MaxStack import MaxStack
from pyquiz.leetcode.MaxStack import MaxStack


class TestMaxStack(TestCase):
    def test_max_top(self):
        ms = MaxStack()
        ms.push(-2)
        ms.push(0)
        ms.push(-3)
        self.assertEqual(0, ms.peekMax())  # -2 0 -3
        ms.pop()
        self.assertEqual(0, ms.top())  # -2 0
        self.assertEqual(0, ms.peekMax())  # -2 0

    def test_same_val(self):
        ms = MaxStack()
        ms.push(1)
        ms.push(2)
        ms.push(2)
        ms.push(2)
        ms.pop()
        self.assertEqual(2, ms.peekMax())    # 1 2 2 2
        self.assertEqual(2, ms.top())       # 1 2 2 2
        self.assertEqual(2, ms.pop())       # 1 2 2 2
        self.assertEqual(2, ms.peekMax())   # 1 2 2
        self.assertEqual(2, ms.top())       # 1 2 2
        self.assertEqual(2, ms.pop())       # 1 2
        self.assertEqual(1, ms.peekMax())   # 1 2
        self.assertEqual(1, ms.top())       # 1 2
        self.assertEqual(1, ms.pop())       # 1
        self.assertIsNone(ms.pop())         #
        self.assertIsNone(ms.peekMax())     #
        self.assertIsNone(ms.top())         #

    def test_empty(self):
        ms = MaxStack()
        self.assertIsNone(ms.peekMax())
        self.assertIsNone(ms.top())
        self.assertIsNone(ms.pop())
        ms.push(1)
        ms.pop()
        self.assertIsNone(ms.peekMax())
        self.assertIsNone(ms.top())
        self.assertIsNone(ms.pop())

    def test_badcase(self):
        ms = MaxStack()
        ms.push(5)
        ms.push(1)
        ms.push(5)
        self.assertEqual(5, ms.top()) # 5 1 5
        self.assertEqual(5,ms.popMax()) # 5 1 5
        self.assertEqual(1, ms.top()) # 5 1
        self.assertEqual(5,ms.popMax()) # 5 1
        self.assertEqual(1, ms.top()) # 1
        self.assertEqual(1, ms.peekMax()) # 1
        self.assertEqual(1, ms.pop()) # 1
        self.assertIsNone(ms.top()) #

    def test_push_pop(self):
        ms = MaxStack()
        ms.push(1)
        self.assertEqual(1, ms.top()) #1
        self.assertEqual(1, ms.popMax()) #1
        self.assertIsNone(ms.top())
        self.assertIsNone(ms.pop())
        self.assertIsNone(ms.popMax())

    def test_bad_case2(self):
        ms = MaxStack()
        ms.push(92) #92
        self.assertEqual(92, ms.peekMax()) #92
        ms.push(54) #92 54
        self.assertEqual(92, ms.peekMax()) #92 54
        ms.push(22) #92 54 22
        ms.pop() #92 54
        ms.pop() #92
        ms.push(-57) #92 -57
        self.assertEqual(92, ms.peekMax()) #92 -57
        ms.push(-24) #92 -57 -24
        ms.popMax()
        self.assertEqual(-24, ms.top()) # -57 -24
        ms.push(26) #-57 -24 26
        self.assertEqual(26,ms.peekMax()) #-57 -24 26
        self.assertEqual(26, ms.popMax()) #-57 -24 26
