class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, x):
        self.stack.append(x)
        if not self.mins:
            self.mins.append(x)
        elif self.mins[-1] < x:
            self.mins.append(self.mins[-1])
        else:
            self.mins.append(x)

    def pop(self):
        if self.stack:
            self.stack.pop(-1)
            self.mins.pop(-1)

    def top(self):
        if self.stack: return self.stack[-1]

    def getMin(self):
        if self.mins: return self.mins[-1]
