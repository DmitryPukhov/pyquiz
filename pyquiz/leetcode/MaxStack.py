class MaxStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.m=[]

    def push(self, x: int) -> None:
        if self.stack:
            self.stack.append(x)
            self.m.append(max(x,self.peekMax()))
        else:
            self.stack.append(x)
            self.m.append(x)

    def pop(self) -> int:
        if self.stack:
            self.m.pop()
            return self.stack.pop()
        else:
            return None

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def peekMax(self) -> int:
        return self.m[-1] if self.stack else None

    def popMax(self) -> int:
        xx=[]
        res = None
        while self.stack:
            x = self.stack.pop()
            m = self.m.pop()
            if x == m:
                res = x
                break
            xx.append(x)
        for x in xx[::-1]:
            self.push(x)
        return res
