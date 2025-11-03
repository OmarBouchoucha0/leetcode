class MinStack:

    def __init__(self):
        self.elements = []
        self.min = []

    def push(self, val: int) -> None:
        self.elements.append(val)
        self.min.append(val)
        self.min.sort()

    def pop(self) -> None:
        val = self.elements.pop()
        self.min.remove(val)

    def top(self) -> int:
        return self.elements[-1]

    def getMin(self) -> int:
        return self.min[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
