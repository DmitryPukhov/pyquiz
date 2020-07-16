from unittest import TestCase

from pyquiz.leetcode.QueueUsingStack import QueueUsingStack


class TestQueueUsingStack(TestCase):

    def test_push_pop(self):
        myqueue = QueueUsingStack()
        myqueue.push(1)
        self.assertEqual(1, myqueue.pop())

    def test_pop(self):
        myqueue = QueueUsingStack()
        self.assertIsNone(myqueue.pop())

    def test_pop_push_peek(self):
        myqueue = QueueUsingStack()
        myqueue.pop()
        myqueue.push(1)
        self.assertEqual(1, myqueue.peek())

    def test_push_push(self):
        myqueue = QueueUsingStack()
        myqueue.push(1)
        myqueue.push(2)
        self.assertEqual(1, myqueue.peek())

    def test_push_push_pop_pop(self):
        myqueue = QueueUsingStack()
        myqueue.push(1)
        myqueue.push(2)
        self.assertEqual(1, myqueue.peek())
        self.assertEqual(1, myqueue.pop())
        self.assertEqual(2, myqueue.peek())
        self.assertEqual(2, myqueue.pop())

    def test_empty(self):
        myqueue = QueueUsingStack()
        self.assertTrue(myqueue.empty())

    def test_notempty(self):
        myqueue = QueueUsingStack()
        myqueue.push(1)
        self.assertFalse(myqueue.empty())
