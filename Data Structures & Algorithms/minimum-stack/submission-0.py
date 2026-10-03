class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        # Calculate the running minimum
        val = min(value, self.minStack[-1] if self.minStack else value)
        # BUG FIX: Append 'val' (the minimum), not 'value'
        self.minStack.append(val) 

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

        
