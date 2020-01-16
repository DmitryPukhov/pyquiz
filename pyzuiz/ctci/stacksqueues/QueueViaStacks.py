import queue
from collections import deque

from numpy import stack


class MyQueueViaStacks:
    """
    Queue via Stacks:
    Hints: #98, #7 74
    Implement a MyQueue class which implements a queue using two stacks.
    """
    _left_stack: stack = []
    _left_stack_size = 0
    _right_stack = []
    _right_stack_size = 0

    def put(self, val):
        """
        Queue method: put to the head
        """
        self._left_stack.append(val)
        self._left_stack_size += 1

    def push(self, val):
        self._right_stack.append(val)
        self._right_stack_size += 1

    def pop(self):
        # Rebalance if right stack is empty
        if self._right_stack_size == 0:
            self._rebalance()

        if self._right_stack_size > 0:
            # Pop from right
            self._right_stack_size -= 1
            return self._right_stack.pop()
        elif self._left_stack_size == 1:
            # The only item could be in left stack
            self._left_stack_size -= 1
            return self._left_stack.pop()
        else:
            return None

    def get(self):
        """
        Queue method; get and remove from the head
        """
        # Rebalance if left stack became empty
        if self._left_stack_size == 0:
            self._rebalance()

        # Get from left stack
        if self._left_stack_size > 0:
            # Normal case - get from the left
            self._left_stack_size -= 1
            return self._left_stack.pop()
        elif self._right_stack_size == 1:
            # The only item could be in right stack
            self._right_stack_size -= 1
            return self._right_stack.pop()
        else:
            # Here left stack is empty, so rebalance and try again
            return None

    def _rebalance(self):
        """
        Make left/right stacks sizes equal or +-1
        """
        # how much items will be moved
        delta = abs(self._left_stack_size - self._right_stack_size) // 2
        # It is allowed to use stack only, and we revert left/right stack to tmp stacks

        tmp_right = []
        tmp_left = []
        if delta >= 1:
            for i in range(0, self._right_stack_size):
                tmp_right.append(self._right_stack.pop())
            for i in range(0, self._left_stack_size):
                tmp_left.append(self._left_stack.pop())

        if delta >= 1 and self._left_stack_size > self._right_stack_size:
            # Move extra items from left to right
            for i in range(0, delta):
                self._right_stack.append(tmp_left.pop())
            for i in range(0, self._right_stack_size):
                self._right_stack.append(tmp_right.pop())
            # Move back from tmp to left
            for i in range(0, self._left_stack_size - delta):
                self._left_stack.append(tmp_left.pop())
            # Update sizes
            self._left_stack_size -= delta
            self._right_stack_size += delta
        elif delta >= 1 and self._right_stack_size > self._left_stack_size:
            # Move extra items from right to left
            for i in range(0, delta):
                self._left_stack.append(tmp_right.pop())
            for i in range(0, self._left_stack_size):
                self._left_stack.append(tmp_left.pop())
            # Move back from tmp to right
            for i in range(0, self._right_stack_size - delta):
                self._right_stack.append(tmp_right.pop())
            # Update sizes
            self._right_stack_size -= delta
            self._left_stack_size += delta
