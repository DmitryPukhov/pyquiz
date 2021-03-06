from unittest import TestCase

from pyquiz.ctci.stacksqueues.StackMin import StackMin


class TestStackMin(TestCase):

    def test_pushpop(self):
        stack = StackMin()
        stack.push(3)
        assert stack.min() == 3
        stack.push(1)
        assert stack.min() == 1
        stack.push(2)
        assert stack.min() == 1

        assert stack.pop() == 2
        assert stack.min() == 1
        assert stack.pop() == 1
        assert stack.min() == 3
        assert stack.pop() == 3
        assert stack.min() is None
        assert stack.pop() is None
