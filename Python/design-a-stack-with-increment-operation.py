class CustomStack:

    def __init__(self, maxSize):
        self.size = maxSize
        self.arr = []
        self.incs = []

    def push(self, x):
        if len(self.arr) < self.size: self.arr.append(x)

    def pop(self):
        if not len(self.arr): return -1
        for i, inc in enumerate(self.incs):
            if inc[0] == len(self.arr):
                self.incs[i] = (inc[0] - 1, inc[1])
                self.arr[-1] += inc[1]
            elif inc[0] < len(self.arr):
                break

        return self.arr.pop(-1)

    def increment(self, k, val):
        if k > len(self.arr):
            k = len(self.arr)
        self.incs.append((k, val))
        self.incs = sorted(self.incs, reverse=True)

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
