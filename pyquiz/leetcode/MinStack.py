from heapq import heappush, heappop, nsmallest


class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    push(x) -- Push element x onto stack.
    pop() -- Removes the element on top of the stack.
    top() -- Get the top element.
    getMin() -- Retrieve the minimum element in the stack.


    Constraints:
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    Accepted
    566,397
    Submissions
    1,278,050
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []

    def push(self, x: int) -> None:
        self.s.append((x, min(x, self.getMin()) if self.s else x))

    def pop(self) -> None:
        # ???
        return self.s.pop()[0] if self.s else None

    def top(self) -> int:
        return self.s[-1][0] if self.s else None

    def getMin(self) -> int:
        return self.s[-1][1] if self.s else None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
