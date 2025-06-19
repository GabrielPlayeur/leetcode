class MinStack:

    def __init__(self):
        self.s = []
        self.mS = []

    def push(self, val: int) -> None:
        self.s.append(val)
        self.mS.append(min(val, self.mS[-1] if self.mS else val))

    def pop(self) -> None:
        self.s.pop()
        self.mS.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.mS[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
