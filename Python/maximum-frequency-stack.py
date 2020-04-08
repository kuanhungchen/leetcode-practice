class FreqStack:

    def __init__(self):
        self.freqs = {}
        self.max_freq = 0
        self.stack = {}

    def push(self, x):
        if x in self.freqs:
            f = self.freqs[x] + 1
        else:
            f = 1
        self.freqs[x] = f
        self.max_freq = max(self.max_freq, f)
        if f in self.stack:
            self.stack[f].append(x)
        else:
            self.stack[f] = [x]

    def pop(self):
        ans = self.stack[self.max_freq].pop(-1)
        self.freqs[ans] -= 1
        if not self.stack[self.max_freq]:
            self.max_freq -= 1

        return ans

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
