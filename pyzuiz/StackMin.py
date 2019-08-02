from pyzuiz.tools.DoubleLinkedNode import DoubleLinkedNode


class StackMin:
    """
    Stack Min: How would you design a stack which, in addition to push and pop,
    has a function min which returns the minimum element?
    Push, pop and min should all operate in 0(1) time

    Solution: track current min/max item along with stack items
    """

    def __init__(self):
        # Stack of values
        self._tail_val: DoubleLinkedNode = None
        # Stack of minimums
        self._tail_min: DoubleLinkedNode = None

    def push(self, value):

        if self._tail_val is None:
            # No tail yet, first item in the stack
            self._tail_val = DoubleLinkedNode(value)
            self._tail_min = DoubleLinkedNode(value)
        else:
            # Add to existing tail
            self._tail_val.next_ = DoubleLinkedNode(value, self._tail_val, None)
            self._tail_val = self._tail_val.next_

            # Push new minimum to min stack
            new_min = min(self._tail_min.value, value)
            self._tail_min.next_ = DoubleLinkedNode(new_min, self._tail_min, None)
            self._tail_min = self._tail_min.next_

    def pop(self):
        if self._tail_val is None:
            return None

        # Take last node
        node_val: DoubleLinkedNode = self._tail_val

        # Set tail to prev node for both minimums and values stack
        if node_val.prev is not None:
            # Remove last node, previous exists and will be a new tail
            self._tail_val = node_val.prev
            self._tail_val.next = None

            self._tail_min = self._tail_min.prev
            self._tail_min.next = None
        else:
            # First element removed, none left
            self._tail_val = None
            self._tail_min = None

        return node_val.value

    def min(self):
        """
        Return minimum value, no modification of the stack.
        :return: minimum of the stack according to quiz requirement
        """
        return self._tail_min.value if self._tail_min is not None else None
