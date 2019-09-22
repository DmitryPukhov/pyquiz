from unittest import TestCase

from pyzuiz.stacksqueues.SetOfStacks import SetOfStacks


class TestSetOfStacks(TestCase):

    def test_push(self):
        stack: SetOfStacks = SetOfStacks(2)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)

        self.assertEqual(1, stack._stacks[0][0])
        self.assertEqual(2, stack._stacks[0][1])
        self.assertEqual(3, stack._stacks[1][0])
        self.assertEqual(4, stack._stacks[1][1])

    def test_pop(self):
        stack: SetOfStacks = SetOfStacks(2)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(4, stack.pop())
        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())

    def test_pop__empty__error(self):
        stack = SetOfStacks(2)
        self.assertRaises(BaseException, stack.pop)

    def test_pop_at(self):
        stack: SetOfStacks = SetOfStacks(2)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(2, stack.pop_at(0))
        self.assertEqual(4, stack.pop_at(1))

    def test_pop_at__bad_index__error(self):
        stack: SetOfStacks = SetOfStacks(2)
        self.assertRaises(BaseException, stack.pop_at, 1)

