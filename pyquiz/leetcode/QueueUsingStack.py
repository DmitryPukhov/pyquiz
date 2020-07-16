class QueueUsingStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack: self.front = x
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        tmp = []
        while self.stack: tmp.append(self.stack.pop())
        out = tmp.pop() if tmp else None
        self.front = tmp[-1] if tmp else None
        while tmp: self.stack.append(tmp.pop())
        return out

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.stack


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()