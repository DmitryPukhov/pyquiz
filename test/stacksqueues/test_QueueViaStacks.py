from unittest import TestCase

from pyzuiz.stacksqueues.QueueViaStacks import MyQueueViaStacks


class TestMyQueueViaStacks(TestCase):
    def test_put(self):
        q = MyQueueViaStacks()
        q.put(1)
        self.assertEqual([1], q._left_stack)
        self.assertEqual(1, q._left_stack_size)

    def test_pushpop(self):
        # Queue 1,2,3,4
        q = MyQueueViaStacks()
        q.put(2)
        q.push(3)
        q.put(1)
        q.push(4)

        self.assertEqual(1, q.get())
        self.assertEqual(4, q.pop())
        self.assertEqual(2, q.get())
        self.assertEqual(3, q.pop())
        self.assertIsNone(q.get())
        self.assertIsNone(q.pop())

    def test_push(self):
        q = MyQueueViaStacks()
        q.push(1)
        self.assertEqual([1], q._right_stack)
        self.assertEqual(1, q._right_stack_size)

    def test_get(self):
        q = MyQueueViaStacks()
        q._left_stack = [1]
        q._left_stack_size = 1
        val = q.pop()
        empty_val = q.pop()
        self.assertEqual(1, val)
        self.assertEqual(0, q._left_stack_size)
        self.assertIsNone(empty_val)

    def test_get__the_only_item_on_the_left(self):
        q = MyQueueViaStacks()
        q._right_stack = [1]
        q._right_stack_size = 1
        val = q.pop()
        empty_val = q.pop()
        self.assertEqual(1, val)
        self.assertEqual(0, q._right_stack_size)
        self.assertIsNone(empty_val)

    def test_pop(self):
        q = MyQueueViaStacks()
        q._right_stack = [1]
        q._right_stack_size = 1
        val = q.pop()
        empty_val = q.pop()
        self.assertEqual(1, val)
        self.assertEqual(0, q._right_stack_size)
        self.assertIsNone(empty_val)

    def test_pop__the_only_item_on_the_left(self):
        q = MyQueueViaStacks()
        q._left_stack = [1]
        q._left_stack_size = 1
        val = q.pop()
        empty_val = q.pop()
        self.assertEqual(1, val)
        self.assertEqual(0, q._left_stack_size)
        self.assertIsNone(empty_val)

    def test__rebalance__right2left_delta3(self):
        # Prepare unbalanced queue
        q = MyQueueViaStacks()
        q._left_stack = [1]
        q._left_stack_size = 1

        q._right_stack = [2, 3, 4, 5]
        q._right_stack_size = 4

        # Do rebalance
        q._rebalance()

        self.assertEqual([2, 1], q._left_stack)
        self.assertEqual(2, q._left_stack_size)
        self.assertEqual([3, 4, 5], q._right_stack)
        self.assertEqual(3, q._right_stack_size)

    def test__rebalance__left2right_delta3(self):
        # Prepare unbalanced queue
        q = MyQueueViaStacks()
        q._left_stack = [4, 3, 2, 1]
        q._left_stack_size = 4

        q._right_stack = [5]
        q._right_stack_size = 1

        # Do rebalance
        q._rebalance()

        self.assertEqual([3, 2, 1], q._left_stack)
        self.assertEqual(3, q._left_stack_size)
        self.assertEqual([4, 5], q._right_stack)
        self.assertEqual(2, q._right_stack_size)

    def test__rebalance__left2right(self):
        # Prepare unbalanced queue
        q = MyQueueViaStacks()
        q._left_stack = [3, 2, 1]
        q._left_stack_size = 3

        q._right_stack = [4]
        q._right_stack_size = 1

        # Do rebalance
        q._rebalance()

        self.assertEqual([2, 1], q._left_stack)
        self.assertEqual(2, q._left_stack_size)
        self.assertEqual([3, 4], q._right_stack)
        self.assertEqual(2, q._right_stack_size)

    def test__rebalance__right2left(self):
        # Prepare unbalanced queue
        q = MyQueueViaStacks()
        q._left_stack = [1]
        q._left_stack_size = 1

        q._right_stack = [2, 3, 4]
        q._right_stack_size = 3

        # Do rebalance
        q._rebalance()

        self.assertEqual([2, 1], q._left_stack)
        self.assertEqual(2, q._left_stack_size)
        self.assertEqual([3, 4], q._right_stack)
        self.assertEqual(2, q._right_stack_size)
