class SetOfStacks:
    """
    Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
    threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
    composed of several stacks and should create a new stack once the previous one exceeds capacity.
    SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
    (that is, pop () should return the same values as it would if there were just a single stack).
    FOLLOW UP
    Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
    Hints:#64, #87
    pg233
    """

    def __init__(self, threshold: int):
        # Set first empty stack to be current
        self._stacks = [[]]
        self._cur_stack_index = 0
        self._threshold = threshold

    def push(self, val):
        stack = self._stacks[self._cur_stack_index]
        if len(stack) >= self._threshold:
            # Current stack if full, add a new one
            self._stacks.append([val])
            self._cur_stack_index += 1
        else:
            stack.append(val)

    def pop(self):
        # Pop from current stack
        stack = self._stacks[self._cur_stack_index]
        val = stack.pop()

        if len(stack) == 0 and self._cur_stack_index > 0:
            # Remove current stack if it is empty and not first stack
            self._stacks.pop()
            self._cur_stack_index -= 1
        return val

    def pop_at(self, index: int):
        stack = self._stacks[index]
        return stack.pop()
